""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton("•🗣️ Sᴜᴘᴘᴏʀᴛ•", url="t.me/SHIZUKA_SUPPORT"),
      InlineKeyboardButton("•📣 Uᴘᴅᴀᴛᴇs•", url="t.me/SHIZUKA_UPDATES"),
     ],
     [
      InlineKeyboardButton("•Oᴡɴᴇʀ•", url="t.me/pratheek06"),
     ]
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="End⏹", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="Pause⏸", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="Resume▶️", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="Mute🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="Unmute🔊", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🗑 Close", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Back", callback_data="cbmenu"
      )
    ]
  ]
)
