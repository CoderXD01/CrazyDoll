from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ✘ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 🥀 ✘",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✘ 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 ✘",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✘ 𝙎𝙀𝙏𝙏𝙄𝙉𝙂𝙎 ✘", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✘ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 ✘",
                url=f"https://t.me/the_iconic_support",
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✘ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 ✘",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✘ 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 ✘", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✘ 𝙐𝙋𝘿𝘼𝙏𝙀𝙎 ✘", url=f"https://t.me/iconic_botshub",
            )
        ],
        [
            InlineKeyboardButton(
                text="✘ 𝘾𝙃𝘼𝙏𝙏𝙄𝙉𝙂𝙎 ✘", url=f"https://t.me/english_hindi_group_chat",
            ),
            InlineKeyboardButton(
                text="✘ 𝙁𝙀𝙀𝙇𝙄𝙉𝙂𝙎 ✘", url=f"https://t.me/about_abhi_i",
            )
        ],
        [
            InlineKeyboardButton(
                text="✘ 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 ✘", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
