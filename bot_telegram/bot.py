from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Substitua 'TOKEN' pelo token do seu bot
TOKEN = 'seu_token_aqui'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Eu sou um bot Telegram.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
