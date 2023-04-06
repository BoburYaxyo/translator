import logging

import requests
import json
from oxfordapi import get_definitons




from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
translator = Translator()

API_TOKEN = '6181650817:AAFP2gj-VLpOEBQwQedFNL_363SR431gu8w'


# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Salom speakenglish botga xush kelibsiz!")



@dp.message_handler()
async def tarjimon(message: types.Message):
    lang=translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)

    else:
        if lang=='en':
            word_id=message.text
        else:
            word_id=translator.translate(message.text, dest='en').text
        lookup=get_definitons(word_id)
        if lookup:
            await message.reply(f"Word {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply('Bunday so\'z topilmadi')




if __name__ == '__main__':
    executor.start_polling(dp)


