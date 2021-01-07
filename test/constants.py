from aenum import Enum, NoAlias

from discord import Color

tortoise_guild_id = 577192344529404154
website_url = "https://www.tortoisecommunity.com/"
privacy_url = "https://www.tortoisecommunity.com/pages/privacy"
rules_url = "https://www.tortoisecommunity.com/pages/rules"
verification_url = "https://www.tortoisecommunity.com/verification/"
github_repo_link = "https://github.com/Tortoise-Community/Tortoise-BOT"
tortoise_paste_service_link = "https://paste.tortoisecommunity.com/"
tortoise_paste_endpoint = "https://paste.tortoisecommunity.com/documents/"
line_img_url = "https://cdn.discordapp.com/attachments/649868379372388352/723173852796158062/animated-line.gif"
github_repo_stats_endpoint = "https://api.github.com/repos/Tortoise-Community/"
project_url = "https://www.tortoisecommunity.com/pages/projects/"

# Channel IDs
welcome_channel_id = 738731842538176522
announcements_channel_id = 578197131526144024
react_for_roles_channel_id = 603651772950773761

mod_mail_report_channel_id = 693790120712601610
bug_reports_channel_id = 693790120712601610
code_submissions_channel_id = 610079185569841153
suggestions_channel_id = 708734512296624239

# Log Channel IDs
system_log_channel_id = 593883395436838942
deterrence_log_channel_id = 597119801701433357
bot_log_channel_id = 693090079329091615
successful_verifications_channel_id = 581139962611892229
verification_channel_id = 602156675863937024
website_log_channel_id = 649868379372388352
bot_dev_channel_id = 692851221223964822
error_log_channel_id = 690650346665803777
member_count_channel_id = 723526255495872566
general_channel_id = 577192344533598472

# Roles
muted_role_id = 707007421066772530
verified_role_id = 599647985198039050
trusted_role_id = 703657957438652476
moderator_role = 577368219875278849
admin_role = 577196762691928065
new_member_role = 743751537305845813

# Keys are IDs of reaction emojis
# Values are role IDs which will get added if that reaction gets added/removed
self_assignable_roles = {
    582547250635603988: 589128905290547217,     # Python
    603276263414562836: 589129320480636986,     # Javascript
    723277556459241573: 591254311162347561,     # HTML/CSS
    723274176991068261: 589131126619111424,     # SQL
    603275563972689942: 589131022520811523,     # C
    603275529587654665: 589129873809735700,     # C++
    723280469122089131: 589130125208190991,     # C#
    723272019126255726: 589129070609039454,     # Java
    723276957810163731: 589129583375286415,     # R
    610825682070798359: 610834658267103262,     # events
    583614910215356416: 603157798225838101,     # announcements
    782187224195268629: 781210603997757471      # challenges
}


# Emoji IDs
mod_mail_emoji_id = 706195614857297970
event_emoji_id = 611403448750964746
bug_emoji_id = 723274927968354364
suggestions_emoji_id = 613185393776656384
verified_emoji_id = 610713784268357632
upvote_emoji_id = 741202481090002994
hit_emoji_id = 755715814883196958
stay_emoji_id = 755717238732095562
double_emoji_id = 755715816657518622
blank_card_emoji = "<:card:755715225642336287>"

# Badges
partner = "<:partner:753957703155449916>"
staff = "<:staff:753957681336942673>"
nitro = "<:nitro:753957661912989747>"
hs_bal = "<:balance:753957264460873728>"
hs_bril = "<:brilliance:753957311537479750>"
hs_brav = "<:bravery:753957296475996234>"
hs_ev = "<:events:753957640069185637>"
verified_bot_dev = "<:dev:753957609328869384>"
bg_1 = "<:bug1:753957385844031538>"
bg_2 = "<:bug2:753957425664753754>"
ear_supp = "<:early:753957626097696888>"

# Emotes
idle = "🌙"
game_emoji = "🎮"
online = "<:online:753999406562410536>"
offline = "<:offline:753999424446922782>"
dnd = "<:dnd:753999445728952503>"
spotify_emoji = "<:spotify:754238046123196467>"
tick_yes = "<:tickyes:758291659330420776>"
tick_no = "<:tickno:753974818549923960>"
pin_emoji = "<:pinunread:754233175244537976>"
user_emoji = "<:user:754234411922227250>"
git_start_emoji = "<:git_star:758616139646763064>"
git_fork_emoji = "<:git_fork:758616130780004362>"
git_commit_emoji = "<:git_commit:758616123590574090>"
git_repo_emoji = "<:repo:758616137977561119>"
success_emoji = "<:success:781891698590482442>"
failure_emoji = "<:failure:781891692160090143>"

# Icons
google_icon = "https://www.freepnglogos.com/uploads/google-logo-png/" \
              "google-logo-png-google-icon-logo-png-transparent-svg-vector-bie-supply-14.png"
stackof_icon = "https://cdn2.iconfinder.com/data/icons/social-icons-color/512/stackoverflow-512.png"

# Music Options
# For all options see:
# https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0"  # ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}

# Special
tortoise_developers = (197918569894379520, 612349409736392928)

# Embeds are not monospaced so we need to use spaces to make different lines "align"
# But discord doesn't like spaces and strips them down.
# Using a combination of zero width space + regular space solves stripping problem.
embed_space = "\u200b "

# After this is exceeded the link to tortoise paste service should be sent
max_message_length = 1000


class Infraction(Enum):
    _settings_ = NoAlias

    warning = Color.gold()
    kick = Color.gold()
    ban = Color.red()


class SuggestionStatus(Enum):
    under_review = "Under Review"
    denied = "Denied"
    approved = "Approved"


blackjack_player_limit = 4

spade_emotes = {
    "A": "<:sA:755697555505020928>",
    "2": "<:s2:755697541823201292>",
    "3": "<:s3:755697544671133796>",
    "4": "<:s4:755697547921588274>",
    "5": "<:s5:755697547590238281>",
    "6": "<:s6:755697552837443624>",
    "7": "<:s7:755697553198284890>",
    "8": "<:s8:755697553579704430>",
    "9": "<:s9:755697554456313867>",
    "10": "<:s10:755697555303825498>",
    "K": "<:sK:755697557212233738>",
    "Q": "<:sQ:755697557249982497> ",
    "J": "<:sJ:755697555475529790>"
}

club_emotes = {
    "A": "<:cA:755697680797138954>",
    "2": "<:c2:755697675281760357>",
    "3": "<:c3:755697676095455342>",
    "4": "<:c4:755697675923488789>",
    "5": "<:c5:755697676468617267>",
    "6": "<:c6:755697676846104666>",
    "7": "<:c7:755697677060014131>",
    "8": "<:c8:755697676921864273>",
    "9": "<:c9:755697680763846727>",
    "10": "<:c10:755697680449273918>",
    "K": "<:cK:755697681157980200>",
    "Q": "<:cQ:755697681023762454>",
    "J": "<:cJ:755697680881025064>"
}

heart_emotes = {

    "A": "<:hA:755698059094261830>",
    "2": "<:h2:755698046297440287>",
    "3": "<:h3:755698046624596079>",
    "4": "<:h4:755698046821466162>",
    "5": "<:h5:755698046536515605>",
    "6": "<:h6:755698046850957335>",
    "7": "<:h7:755698050466578553>",
    "8": "<:h8:755698056405450773>",
    "9": "<:h9:755698058070589460>",
    "10": "<:h10:755698058989404160>",
    "K": "<:hK:755698058968432652>",
    "Q": "<:hQ:755698059379474552>",
    "J": "<:hJ:755698059056513065>"
}

diamond_emotes = {

    "A": "<:dA:755714705158307952>",
    "2": "<:d2:755709806848901181>",
    "3": "<:d3:755709807486566413>",
    "4": "<:d4:755709807708602368>",
    "5": "<:d5:755709807985688617>",
    "6": "<:d7:755709808555851808>",
    "7": "<:d6:755709808681680917>",
    "8": "<:d8:755709809189191680>",
    "9": "<:d9:755709809323671583>",
    "10": "<:d10:755709809399037963>",
    "K": "<:dk:755714708279001208>",
    "Q": "<:dQ:755714709742813216>",
    "J": "<:dJ:755714707150733353>"
}

card_emotes = {
    "spade": spade_emotes,
    "club": club_emotes,
    "heart": heart_emotes,
    "diamond": diamond_emotes
}

# These are not allowed and will be auto-deleted but we will also upload them to pastebin and provide the link to paste
extension_to_pastebin = (
    "txt",
    "py"
)

# These ones are allowed and will not get auto-deleted by bot.
allowed_file_extensions = (
    "3gp",
    "3g2",
    "avi",
    "bmp",
    "gif",
    "h264",
    "jpg",
    "jpeg",
    "mp3",
    "m4v",
    "mkv",
    "mov",
    "mp4",
    "mpeg",
    "mpg",
    "ogg",
    "png",
    "svg",
    "tiff",
    "wmv",
    "wav",
    "webm"
)
