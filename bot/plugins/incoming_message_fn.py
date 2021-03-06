#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K / Akshay C / @AbirHasan2005

# the logging things

import datetime
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os, time, asyncio, json
from bot.localisation import Localisation
from bot import (
  DOWNLOAD_LOCATION, 
  AUTH_USERS,
  LOG_CHANNEL,
  UPDATES_CHANNEL
)
from bot.helper_funcs.ffmpeg import (
  convert_video,
  media_info,
  take_screen_shot
)
from bot.helper_funcs.display_progress import (
  progress_for_pyrogram,
  TimeFormatter,
  humanbytes
)

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

from bot.helper_funcs.utils import(
  delete_downloads
)
        
async def incoming_start_message_f(bot, update):
    """/start command"""
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await bot.send_message(
                   chat_id=update.chat.id,
                   text="**Sorry Sir, You Are Banned From Using Me. Contact My** [Support Bot](https://t.me/FlixHelpBot).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=update.chat.id,
                text="**Please Join My Updates Channel Below To Use This Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel 📢", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=update.chat.id,
                text="**Something Went Wrong. Contact My** [Support Bot](https://t.me/FlixHelpBot).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await bot.send_message(
        chat_id=update.chat.id,
        text=Localisation.START_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Updates Channel 📢', url='https://t.me/FlixBots')
                ],
                [
                    InlineKeyboardButton('Support Bot 🙎', url='https://t.me/FlixHelpBot')
                ]
            ]
        ),
        reply_to_message_id=update.message_id,
    )
    
async def incoming_compress_message_f(bot, update):
  """/compress command"""
  update_channel = UPDATES_CHANNEL
  if update_channel:
      try:
          user = await bot.get_chat_member(update_channel, update.chat.id)
          if user.status == "kicked":
             await bot.send_message(
                 chat_id=update.chat.id,
                 text="**Sorry Sir, You Are Banned From Using Me. Contact My** [Support Bot](https://t.me/FlixHelpBot).",
                 parse_mode="markdown",
                 disable_web_page_preview=True
             )
             return
      except UserNotParticipant:
          await bot.send_message(
              chat_id=update.chat.id,
              text="**Please Join My Updates Channel Below To Use This Bot!**",
              reply_markup=InlineKeyboardMarkup(
                  [
                      [
                          InlineKeyboardButton("Join Our Updates Channel 📢", url=f"https://t.me/{update_channel}")
                      ]
                  ]
              ),
              parse_mode="markdown"
          )
          return
      except Exception:
          await bot.send_message(
              chat_id=update.chat.id,
              text="**Something Went Wrong. Contact My [Support Bot](https://t.me/FlixHelpBot).",
              parse_mode="markdown",
              disable_web_page_preview=True
          )
          return
  if update.reply_to_message is None:
    try:
      await bot.send_message(
        chat_id=update.chat.id,
        text="🤬 Reply to telegram media 🤬",
        reply_to_message_id=update.message_id
      )
    except:
      pass
    return
  target_percentage = 50
  isAuto = False
  if len(update.command) > 1:
    try:
      if int(update.command[1]) <= 90 and int(update.command[1]) >= 10:
        target_percentage = int(update.command[1])
      else:
        try:
          await bot.send_message(
            chat_id=update.chat.id,
            text="🤬 Value should be 10 to 90",
            reply_to_message_id=update.message_id
          )
          return
        except:
          pass
    except:
      pass
  else:
    isAuto = True
  user_file = str(update.from_user.id) + ".FFMpegRoBot.mkv"
  saved_file_path = DOWNLOAD_LOCATION + "/" + user_file
  LOGGER.info(saved_file_path)
  d_start = time.time()
  c_start = time.time()
  u_start = time.time()
  status = DOWNLOAD_LOCATION + "/status.json"
  if not os.path.exists(status):
    sent_message = await bot.send_message(
      chat_id=update.chat.id,
      text=Localisation.DOWNLOAD_START,
      reply_to_message_id=update.message_id
    )
    chat_id = LOG_CHANNEL
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
    ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
    bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
    bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
    now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
    await bot.send_message(chat_id, f"**Video Compressing Started\n\nBot Status : Busy Now  🔴**\n\n➤ @CompressFlixBot\n\n**A Process Started At** `{now}`", parse_mode="markdown")
    try:
      d_start = time.time()
      status = DOWNLOAD_LOCATION + "/status.json"
      with open(status, 'w') as f:
        statusMsg = {
          'running': True,
          'message': sent_message.message_id
        }

        json.dump(statusMsg, f, indent=2)
      video = await bot.download_media(
        message=update.reply_to_message,
        file_name=saved_file_path,
        progress=progress_for_pyrogram,
        progress_args=(
          bot,
          Localisation.DOWNLOAD_START,
          sent_message,
          d_start
        )
      )
      LOGGER.info(video)
      if( video is None ):
        try:
          await sent_message.edit_text(
            text="Download stopped"
          )
          chat_id = LOG_CHANNEL
          utc_now = datetime.datetime.utcnow()
          ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
          ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
          bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
          bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
          now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
          await bot.send_message(chat_id, f"**Download Stopped ❌\n\nBot Status : Free  🟢**\n\n➤ @CompressFlixBot\n\n**Process Stopped At** `{now}`", parse_mode="markdown")
        except:
          pass
        delete_downloads()
        LOGGER.info("Download stopped")
        return
    except (ValueError) as e:
      try:
        await sent_message.edit_text(
          text=str(e)
        )
      except:
          pass
      delete_downloads()            
    try:
      await sent_message.edit_text(                
        text=Localisation.SAVED_RECVD_DOC_FILE                
      )
    except:
      pass            
  else:
    try:
      await bot.send_message(
        chat_id=update.chat.id,
        text=Localisation.FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🥳 Bot Status 🥳', url='https://t.me/CompressFlixLogs') # Replace With Your's
                ]
            ]
        ),
        reply_to_message_id=update.message_id
      )
    except:
      pass
    return
  
  if os.path.exists(saved_file_path):
    downloaded_time = TimeFormatter((time.time() - d_start)*1000)
    duration, bitrate = await media_info(saved_file_path)
    if duration is None or bitrate is None:
      try:
        await sent_message.edit_text(                
          text="⚠️ Getting video meta data failed ⚠️"                
        )
        chat_id = LOG_CHANNEL
        utc_now = datetime.datetime.utcnow()
        ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
        ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
        bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
        bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
        now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
        await bot.send_message(chat_id, f"**Download Failed ❌**\n\n**Bot Status : Free  🟢**\n\n➤ @CompressFlixBot\n\n**Process Stopped At** `{now}`", parse_mode="markdown")
      except:
          pass          
      delete_downloads()
      return
    thumb_image_path = await take_screen_shot(
      saved_file_path,
      os.path.dirname(os.path.abspath(saved_file_path)),
      (duration / 2)
    )
    await sent_message.edit_text(                    
      text=Localisation.COMPRESS_START                    
    )
    c_start = time.time()
    o = await convert_video(
           saved_file_path, 
           DOWNLOAD_LOCATION, 
           duration, 
           bot, 
           sent_message, 
           target_percentage, 
           isAuto
         )
    compressed_time = TimeFormatter((time.time() - c_start)*1000)
    LOGGER.info(o)
    if o == 'stopped':
      return
    if o is not None:
      await sent_message.edit_text(                    
        text=Localisation.UPLOAD_START,                    
      )
      u_start = time.time()
      caption = Localisation.COMPRESS_SUCCESS.replace('{}', downloaded_time, 1).replace('{}', compressed_time, 1)
      upload = await bot.send_video(
        chat_id=update.chat.id,
        video=o,
        caption=caption,
        supports_streaming=True,
        duration=duration,
        thumb=thumb_image_path,
        reply_to_message_id=update.message_id,
        progress=progress_for_pyrogram,
        progress_args=(
          bot,
          Localisation.UPLOAD_START,
          sent_message,
          u_start
        )
      )
      if(upload is None):
        try:
          await sent_message.edit_text(
            text="Upload stopped"
          )
          chat_id = LOG_CHANNEL
          utc_now = datetime.datetime.utcnow()
          ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
          ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
          bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
          bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
          now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
          await bot.send_message(chat_id, f"**Upload Stopped ❌**\n\n**Bot Status : Free  🟢**\n\n➤ @CompressFlixBot\n\n**Process Stopped At** `{now}`", parse_mode="markdown")
        except:
          pass
        delete_downloads()
        return
      uploaded_time = TimeFormatter((time.time() - u_start)*1000)
      await sent_message.delete()
      delete_downloads()
      chat_id = LOG_CHANNEL
      utc_now = datetime.datetime.utcnow()
      ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
      ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
      bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
      bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
      now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
      await bot.send_message(chat_id, f"**Uploaded Successfully 🎦**\n\n**Bot Status : Free  🟢**\n\n➤ @CompressFlixBot\n\n**Process Done At** `{now}`", parse_mode="markdown")
      LOGGER.info(upload.caption);
      try:
        await upload.edit_caption(
          caption=upload.caption.replace('{}', uploaded_time)
        )
      except:
        pass
    else:
      delete_downloads()
      try:
        await sent_message.edit_text(                    
          text="⚠️ Compression failed ⚠️"               
        )
        chat_id = LOG_CHANNEL
        utc_now = datetime.datetime.utcnow()
        ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
        ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
        bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
        bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
        now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
        await bot.send_message(chat_id, f"**Compression Failed 📀**\n\n**Bot Status : Free  🟢**\n\n➤ @CompressFlixBot\n\n**Process Stopped At** `{now}`", parse_mode="markdown")
      except:
        pass
      
  else:
    delete_downloads()
    try:
      await sent_message.edit_text(                    
        text="⚠️ Failed To Download, Path  Does Not Exist ⚠️"               
      )
      chat_id = LOG_CHANNEL
      utc_now = datetime.datetime.utcnow()
      ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)
      ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
      bst_now = utc_now + datetime.timedelta(minutes=00, hours=6)
      bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
      now = f"\n{ist} (GMT+05:30)`\n`{bst} (GMT+06:00)"
      await bot.send_message(chat_id, f"**Download Error ‼️**\n\n**Bot Status : Free  🟢**\n\n➤ @CompressFlixBot\n\n**Process Stopped At** `{now}`", parse_mode="markdown")
    except:
      pass
    
async def incoming_cancel_message_f(bot, update):
  """/cancel command"""
  if update.from_user.id not in AUTH_USERS:
    try:
      await update.message.delete()
    except:
      pass
    return

  status = DOWNLOAD_LOCATION + "/status.json"
  if os.path.exists(status):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton("Yes 🚫", callback_data=("fuckingdo").encode("UTF-8")))
    ikeyboard.append(InlineKeyboardButton("No 🤗", callback_data=("fuckoff").encode("UTF-8")))
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await update.reply_text("Are you sure? 🚫 This will stop the compression!", reply_markup=reply_markup, quote=True)
  else:
    delete_downloads()
    await bot.send_message(
      chat_id=update.chat.id,
      text="No active compression exists",
      reply_to_message_id=update.message_id
    )
