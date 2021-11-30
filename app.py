import os
import requests

from flask import Flask, request, jsonify
from flask_caching import Cache  # Import Cache from flask_caching module

import python_weather
import asyncio
import json


app = Flask(__name__)
app.config.from_object('config.Config')  # Set the configuration variables to the flask application
cache = Cache(app)  # Initialize Cache

@app.route("/universities")
@cache.cached(timeout=30, query_string=True)
def get_universities():
  API_URL = "http://universities.hipolabs.com/search?country="
  search = request.args.get('country')
  r = requests.get(f"{API_URL}{search}")
  return jsonify(r.json())

@app.route("/weather")
@cache.cached(timeout=30, query_string=True)
def get_weather():
  # API_URL = "https://api.openweathermap.org/data/2.5/onecall"
  # payload = {'appid': os.environ['WEATHER_APP_ID'], 'lat': '39.952583', 'lon': '-75.165222'}
  
  city = request.args.get('city')

  # r = requests.get(f"{API_URL}", params=payload)

  loop = asyncio.get_event_loop()
  weather = loop.run_until_complete(getweather(city))

  # returns the current day's forecast temperature (int)
  print(weather.current.temperature)

  return jsonify(json.dumps(weather.current))

@app.route('/')
def hello():
  return "Hello World!"

async def getweather(city):
  # declare the client. format defaults to metric system (celcius, km/h, etc.)
  client = python_weather.Client(format=python_weather.IMPERIAL)

  # fetch a weather forecast from a city
  weather = await client.find(city)

  # returns the current day's forecast temperature (int)
  print(weather.current.temperature)

  # get the weather forecast for a few days
  for forecast in weather.forecasts:
      print(str(forecast.date), forecast.sky_text, forecast.temperature)

  # close the wrapper once done
  await client.close()

  return weather


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host = '0.0.0.0', port = port)