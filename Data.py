# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Start The Bot
 ├ /about - About This Bot
 ├ /help - Help Docs & Command List
 ├ /ping - To Check If The Bot Is Alive
 └ /uptime - To See The Bot Stats
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - To View Bot Logs
 ├ /setvar - To Set Var With The command In Bot
 ├ /delvar - To Delete Var With The command In Bot
 ├ /getvar - To View One Of The Vars With The command In Bot
 ├ /users - To View Bot User Statistics
 ├ /batch - To Create Links To More Than One File
 ├ /speedtest - Test The Speed Of Bot Server
 └ /broadcast - Send Broadcast Message To Bot Users

👨‍💻 Develoved By </b><a href='https://t.me/BinaryBandiT69'>@BinaryBandiT69</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About This Bot:

@{} Is A Telegram Bot For Saving Posts Or Files That Can Be Accessed Via A Special Link.

👨‍💻 Develoved By </b><a href='https://t.me/BinaryBandiT69'>@BinaryBandiT69</a>
"""
