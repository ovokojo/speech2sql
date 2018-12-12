from flask import Flask, render_template
import sqlite3
from flask import g

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/experiment")
def model():
  return render_template('SQLmodel.html')

if __name__ == '__main__':
  app.run(debug=True)
