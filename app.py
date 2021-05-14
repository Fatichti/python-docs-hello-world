from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    valeur = input("Valeur test =")
    print("valeur = ",valeur)
    return "Hello, World!"
