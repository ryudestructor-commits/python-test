import os
import telebot

# Carga el token de manera segura desde Render
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def enviar_bienvenida(message):
    nombre = message.from_user.first_name
    texto = f"¡Hola, {nombre}! 👋\n\nSoy **Caza Errores Top**, tu bot personal ya funcionando 24/7."
    bot.reply_to(message, texto, parse_mode="Markdown")

bot.infinity_polling()
