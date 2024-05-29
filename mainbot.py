# credits to telethon quickstart guide

import logging
import re

from telethon.tl.functions.bots import SetBotCommandsRequest
from telethon.tl.types import BotCommandScopeDefault
from telethon import TelegramClient, events

import config
from screenshotter import screenshot

# might be redundant?
actual_username = config.username # will be replaced later in start_up_tasks

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

# The first parameter is the .session file name (absolute paths allowed)
bot = TelegramClient('bot', config.app_id, config.app_hash).start(bot_token=config.bot_token)


# So turns out command registered, do not need an @botname
# @botname by itself still cannot trigger the bot
@bot.on(events.NewMessage(pattern=rf'/{config.command_word_web_img}.*'))
async def handler(event):
    chat_id = await event.get_chat()

    async with bot.action(chat_id, 'typing'):
        message = event.message
        text = message.message
        # logging.info(f"Message received: {message}")
        # logging.info(f"mentioned in chat {chat_id}")

        user = await event.get_sender()
        user_id = user_id.id
        user_name = user_id.username

        if user_id not in config.allowed_users:
            logging.warning(f"Invalid user {user_name} {user_id} tried to access this bot: {event}")
            # won't do anything just return
            return
        logging.info(f"User in whitelist {user_name}")

        try:
            url_matches = re.findall(config.url_regex, text)
            if len(url_matches) == 0:
                # Replies to the message (as a reply). 
                # Shorthand for telethon.client.messages.MessageMethods.send_message 
                # with both entity and reply_to already set.
                await message.reply("No valid url found")
                return
            logging.info(f"url matches: {url_matches}")
            url = url_matches[0][0].strip()
            # url  = message.media.url
            # await message.reply(f"Taking a pic of {url}")
            file_name = await screenshot(url)
            await message.reply(f"[OK] Screenshot of `{url}` taken",
                                file=file_name, force_document=False)
        except Exception as e:
            logging.exception(e)
            await message.reply(f"[Error]: {e}")


# update username in case it changed or something
# update 
async def start_up_tasks():
    me = await bot.get_me()
    username = me.username
    logging.info(f"username: {username}")
    result = await bot(SetBotCommandsRequest(
        scope=BotCommandScopeDefault(),
        lang_code='en',
        commands=config.commands_description_list
    ))
    logging.info(f"Set commands result: {result}")
    return username


bot.start()
actual_username = bot.loop.run_until_complete(start_up_tasks())
bot.run_until_disconnected()

