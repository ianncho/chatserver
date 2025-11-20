from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# MODELO QUE VAS A USAR
MODEL = "x-ai/grok-4.1-fast"

# RUTA PRINCIPAL
@app.route("/", methods=["GET"])
def home():
    return "Servidor funcionando correctamente."

# RUTA PARA EL CHAT
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "")

    headers = {
        "Authorization": f"Bearer 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",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Tenés que ser lo más conciso posible."},
            {"role": "user", "content": mensaje}
        ]
    }

    try:
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers,
            timeout=20
        )
        r.raise_for_status()

        respuesta = r.json()["choices"][0]["message"]["content"]
        return jsonify({"respuesta": respuesta})

    except Exception as e:
        print("Error:", e)
        return jsonify({"respuesta": "error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT",))
    app.run(host="0.0.0.0", port=port)
