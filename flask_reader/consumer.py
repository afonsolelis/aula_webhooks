import pika
import sqlite3

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue='input_queue')

# Conexão com o SQLite
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Criação da tabela se não existir
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, subject TEXT)''')

# Função para gravar mensagem no SQLite
def callback(ch, method, properties, body):
    message = eval(body)  # Converte a mensagem em um dicionário Python
    print("Received:", message)

    # Grava a mensagem no banco de dados SQLite
    c.execute("INSERT INTO messages (name, subject) VALUES (?, ?)", (message['name'], message['subject']))
    conn.commit()

# Consumindo mensagens da fila
channel.basic_consume(queue='input_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()
