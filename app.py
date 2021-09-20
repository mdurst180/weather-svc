import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/universities")
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())

@app.route('/')
def hello():
  return "Hello World!"

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host = '0.0.0.0', port = port)