from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8853292939:AAGlYgIqlDfofnxj4xh9KrWTOaffDgsiwNQ"

@app.route(f"/{TOKEN}", methods=["POST"])
def receive_update():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        if text == "/start":
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            payload = {"chat_id": chat_id, "text": "¡Hola! ¿Qué error cazamos hoy?"}
            requests.post(url, json=payload)
            
    return "ok", 200

@app.route("/")
def index():
    return "¡Bot de Telegram en marcha!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
