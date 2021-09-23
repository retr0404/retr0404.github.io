from flask import Flask, request,render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')



@app.route("/pisos")
def pisos():
    return render_template('pisos.html', name='')

app.run()