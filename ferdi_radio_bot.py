from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from credentials import TELEGRAM_TOKEN
from pydub import AudioSegment, effects

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I bims, eins Ferdi Radio, schick mir eine Sprachnachricht!")

def voice_handler(update, context):
    file = context.bot.getFile(update.message.voice.file_id)
    audio_file = file.download('tmp.ogg')
    audio = AudioSegment.from_ogg('tmp.ogg')
    effects.normalize(audio)
    audio.export('files/' + update.message.chat.first_name + '-' + str(update.message.date) + '.mp3', format="mp3")
    update.message.reply_text("Danke " + update.message.chat.first_name + ", Ferdi freut sich jetzt schon!!!")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(MessageHandler(Filters.voice, voice_handler))





updater.start_polling()

