from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
import os
from dotenv import load_dotenv
import logging


load_dotenv()
TOKEN = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# write a handler for when the bot is started : /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am a Bot!")

# write a handler to echo user input
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def welcome(update: Update, context:ContextTypes.DEFAULT_TYPE):
    new_members = update.message.new_chat_members
    for member in new_members:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {member.name}!\nWelcome to {update.effective_chat.title}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler(command= 'start', callback= start)
    caps_handler = CommandHandler(command= 'caps', callback= caps)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    new_user_handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, callback=welcome)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(new_user_handler)

    # run the app until ctrl+c is pressed
    application.run_polling()
