from django.urls import path
from .views import RenewSubscription, AppStatusUpdate, AppConfirmationView, CustomerDataView


urlpatterns = [

    path('subscription/renew/', RenewSubscription.as_view(), name='home'),
    path('app/status/<str:app_id>/', AppStatusUpdate.as_view(), name='status'),
    path('subscription/refund/', AppConfirmationView.as_view(), name='refund'),
    path('customer/<int:c_id>/', CustomerDataView.as_view(), name="customer_data"),
    path('customer/', CustomerDataView.as_view(), name="customer"),
]
