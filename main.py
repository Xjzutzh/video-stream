import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("ABOUTPRATHEEK")
    await user.join_chat("SHIZUKA_UPDATES")
    await user.join_chat("LYNX_X_UPDATES")
    await user.join_chat("Music_WorldxD")
    await user.join_chat("SHIZUKA_SUPPORT")
    await user.join_chat("LYNX_X_SUPPORT")
    await user.join_chat("https://t.me/+ZlNQgFR1VrBlNTY1")
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
