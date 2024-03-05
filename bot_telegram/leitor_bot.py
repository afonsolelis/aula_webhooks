import sqlite3
import telegram
from telegram.ext import Updater
import time

# Configurações do bot do Telegram
TOKEN = 'seu_token_aqui'
CHAT_ID = 'id_do_chat_aqui'

# Função para enviar mensagem para o Telegram
def send_message(message):
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

# Função para monitorar o banco de dados SQLite em busca de novas entradas
def monitor_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Último ID lido
    last_id = 0

    while True:
        c.execute("SELECT * FROM messages WHERE id > ?", (last_id,))
        new_messages = c.fetchall()

        for message in new_messages:
            # Extrair informações da mensagem do banco de dados
            message_id, name, subject = message

            # Construir mensagem para enviar para o Telegram
            telegram_message = f"Nova mensagem: Nome: {name}, Assunto: {subject}"

            # Enviar mensagem para o Telegram
            send_message(telegram_message)

            # Atualizar o último ID lido
            last_id = message_id

        # Aguardar um tempo antes de verificar novamente o banco de dados
        time.sleep(5)

if __name__ == "__main__":
    monitor_database()
