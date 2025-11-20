    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "tenes que ser lo mas conciso posible"},
            {"role": "user", "content": mensaje}
        ]
    }

    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        r.raise_for_status()
        respuesta = r.json()["choices"][0]["message"]["content"]
        return jsonify({"respuesta": respuesta})
    except Exception as e:
        print("Error:", e)
        return jsonify({"respuesta": "error"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
