from os import name
from flask import Flask, request,render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')



@app.route("/pisos", methods=['POST'])
def pisos():
    name = request.form['name']
    card = request.form['y']
    pincode = request.form['t']
    return render_template('pisos.html', name = name, card = card)

app.run()