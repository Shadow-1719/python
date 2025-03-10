name = "Elias"

from flask import Flask

app = Flask(name)
@app.route('/')
def hello_world():
    return f"Hola {name}!"

if name == 'main':
    app.run(host="0.0.0.0", port=3000)