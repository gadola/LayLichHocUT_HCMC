"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import logging, telegram
from loginUT import loginmain
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CommandHandler, CallbackQueryHandler,CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome to BOT tào lao! nhập help để xem các lệnh')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("""
    /lich : in lịch học
    hết!
    het oi ma
    """)

def lich(update,context):
    update.message.reply_text(update.message.chat.last_name +' chờ xíu nha!!!')
    loginmain()
    pic = r'lich.png'
    context.bot.sendPhoto(chat_id=update.message.chat.id,photo= open(pic,'rb'))

def echo( update, context):
    """Echo the user message."""
    #update is object include inf sender and content
    update.message.reply_text("gọi tui là anh bea nhea!")
    



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1416211526:AAGaimGhqVTbFFgoni2m3idBbKdSGvf769E", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("lich", lich))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

