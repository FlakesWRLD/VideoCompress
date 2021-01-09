#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @AbirHasan2005


from bot.localisation import Localisation
from bot import (
    UPDATES_CHANNEL
)
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

async def new_join_f(client, message):
    # delete all other messages, except for AUTH_USERS
    await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Localisation.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()


async def help_message_f(client, message):
    ## Force Sub ##
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               await message.reply_text(
                   text="Sorry Sir, You Are Banned From Using Me. Contact My [Support Bot](https://t.me/FlixHelpBot).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            await message.reply_text(
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
            await message.reply_text(
                text="Something Went Wrong. Contact My [Support Bot](https://t.me/FlixHelpBot).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    ## Force Sub ##
    await message.reply_text(
        Localisation.HELP_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📢 Updates Channel 📢', url='https://t.me/FlixBots')
                ],
                [
                    InlineKeyboardButton('🗣 Support Group 🗣', url='https://t.me/MirrorZone')
                ],
                [
                    InlineKeyboardButton('Bot Developer 🙎', url='https://t.me/Iggie'),
                    InlineKeyboardButton('Source Code 😍', url='https://t.me/NOSOURCECODE')
                ]
            ]
        ),
        quote=True
    )
