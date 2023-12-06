from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")


#database = {'jason': '123', 'mary': 'xyz', 'johnny': 'abc', 'Tony': 'Ton'}


if (__name__ == "__main__"):
    app.run()
