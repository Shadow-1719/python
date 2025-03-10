from flask import Flask
import os

app = Flask(__name__)  # Usa __name__ en lugar de "Aland"

@app.route('/')
def hello_world():
    return "Hola Aland!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))  # Usa la variable PORT de Render
    app.run(host="0.0.0.0", port=port, debug=True)
