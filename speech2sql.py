from flask import Flask, render_template
import sqlite3
from flask import g
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="http://localhost:5000", allow_headers=[
   "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
   supports_credentials=True, intercept_exceptions=False)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/experiment")
def model():
  return render_template('SQLmodel.html')

if __name__ == '__main__':
  app.run(debug=True)
