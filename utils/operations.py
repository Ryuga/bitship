import os
import shutil
import tarfile
from zipfile import ZipFile

from django.contrib.auth.models import User
from nova_dash.models import Customer, Address, Folder, App, File, Setting
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from utils.handlers import BPDAPIHandler
from django.conf import settings

bpd_api = BPDAPIHandler(token=settings.BPD_SECRET)


def make_tarfile(output_filename, source_dir):
    with tarfile.open(f"media/{output_filename}", "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def create_backup(app, path):
    system_files = ["Procfile", "app.json", "runtime.txt"]
    with ZipFile(os.path.join(settings.MEDIA_ROOT, f"{app.unique_id}_backup.zip"), "w") as backup:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file not in system_files:
                    backup.write(os.path.join(root, file),
                                 os.path.relpath(os.path.join(root, file),
                                                 os.path.join(path, '..')))


def remove_dir_from_storage(path):
    try:
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, path))
    except Exception as E:
        pass


def remove_file_from_storage(path):
    try:
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    except Exception as E:
        pass


def create_customer(user_json: dict, password: str):
    """
    creates new user if the user is not in the database.
    :param user_json: discord oauth2 json data
    :param password: hashed user password
    :return: user: Customer
    """
    user_id = user_json["id"]
    user = User.objects.create_user(username=user_id,
                                    password=password,
                                    is_staff=True,
                                    first_name=user_json["username"],
                                    email=user_json["email"]
                                    )
    customer = Customer.objects.create(id=user_id,
                                       user=user,
                                       credits=0,
                                       tag=user_json["discriminator"],
                                       avatar=user_json["avatar"])
    Address.objects.create(customer=customer)
    Setting.objects.create(customer=customer)
    return customer


def update_customer(user_json: dict):
    user_id = user_json["id"]
    try:
        user = Customer.objects.get(id=user_id)
        user.avatar = user_json["avatar"]
        user.tag = str(user_json["discriminator"])
        user.user.first_name = user_json["username"]
        user.save()

    except Exception as e:
        print("Exception", e)
        # TODO:  attach webhook


@receiver(post_save, sender=App)
def create_app_folder(sender, instance, created, **kwargs):
    if created:
        Folder.objects.create(owner=instance.owner, name=instance.name, app=instance)


@receiver(post_save, sender=File)
def update_folder_size_on_create(sender, instance, created, **kwargs):
    if created:
        folder = instance.folder
        while folder.folder:
            folder.size += instance.size
            folder.save()
            folder = folder.folder


@receiver(post_delete, sender=File)
def update_folder_size_on_delete(sender, instance, **kwargs):
    folder = instance.folder
    while folder.folder:
        folder.size -= instance.size
        folder.save()
        folder = folder.folder
    if instance.item:
        if os.path.isfile(instance.item.path):
            os.remove(instance.item.path)


@receiver(post_delete, sender=App)
def terminate_app_on_delete(sender, instance, **kwargs):
    bpd_api.terminate(instance.unique_id)
