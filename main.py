import os
import telebot
from flask import Flask

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def enviar_bienvenida(message):
    nombre = message.from_user.first_name
    bot.reply_to(message, f"¡Hola, {nombre}! 👋\n\nSoy tu bot y ya estoy activo.")

@server.route('/')
def index():
    return "¡Bot de Telegram en marcha!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    server.run(host="0.0.0.0", port=port)

