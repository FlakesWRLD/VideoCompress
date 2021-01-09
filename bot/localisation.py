#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "<b>Hello, My Name Is 𝗖𝗢𝗠𝗣𝗥𝗘𝗦𝗦 𝗙𝗟𝗜𝗫 𝗥𝗢𝗕𝗢𝗧 🥳.\n\nI'm A <u>𝗩𝗜𝗗𝗘𝗢 𝗖𝗢𝗠𝗣𝗥𝗘𝗦𝗦𝗢𝗥 𝗕𝗢𝗧</u>\n\nSend Me Any 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 Be It 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁/𝗦𝘁𝗿𝗲𝗮𝗺𝗮𝗯𝗹𝗲 & I'll 𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀 It & Resend You A Smaller Packed Size. \n\nSee /help For More Information\n\n❌ 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗢𝗡𝗟𝗬 𝗣𝗘𝗥𝗙𝗢𝗥𝗠 <u>𝗢𝗡𝗘 𝗢𝗣𝗘𝗥𝗔𝗧𝗜𝗢𝗡</u> 𝗧𝗢 𝗔𝗩𝗢𝗜𝗗 𝗕𝗢𝗧 𝗢𝗩𝗘𝗥𝗟𝗢𝗔𝗗.\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗘𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗕𝗼𝘁𝘀</b>"
    ABS_TEXT = "Please Don't Be Selfish."
    
    FORMAT_SELECTION = "Select The Desired Format: <a href='{}'>file size might be approximate</a> \nIf You Want To Set Custom Thumbnail, Send A Photo Before Or Quickly After Tapping On Any Of The Below Buttons.\nYou Can Use /deletethumbnail To Delete The Auto-Generated Thumbnail."
    
    
    DOWNLOAD_START = "<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗩𝗶𝗱𝗲𝗼 𝗧𝗼 𝗠𝘆 𝗦𝗲𝗿𝘃𝗲𝗿 𝗡𝗼𝘄 📁</b>\n"
    
    UPLOAD_START = "<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗧𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗡𝗼𝘄 🌐</b>\n"
    
    COMPRESS_START = "<b>𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀𝗶𝗻𝗴 𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗡𝗼𝘄.. 📀</b>"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 𝟮𝗚𝗕 due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "<b>📁 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗜𝗻 {}</b>\n\n<b>📀 𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀𝗲𝗱 𝗜𝗻 {}</b>\n\n<b>🌐 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗜𝗻 {}</b>\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗘𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗕𝗼𝘁𝘀"

    COMPRESS_PROGRESS = "<b>𝗘𝗧𝗔 :</b> {}\n<b>𝗣𝗿𝗼𝗴𝗿𝗲𝘀𝘀 :</b> {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom Video/File Thumbnail Saved. This Image Will Be Used In The Video/File."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Cleared Succesfully. ❌"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media Cleared Succesfully. ❌"
    
    SAVED_RECVD_DOC_FILE = "𝗠𝗲𝗱𝗶𝗮 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 📩."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail Found. 😒"
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>Bot Is Currently Busy With Another Request Now ⚠️\n\nCheck The Status Of The Bot Below 🔜</b>"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<b><u>More Help & Commands!</u>\n\n<u>Convert To Video</u>\n➠ Send Me Any Telegram File Or Video.\n➠ Reply To That Message With /compress (percentage) Command. Example /compress 50\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗘𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗕𝗼𝘁𝘀</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
