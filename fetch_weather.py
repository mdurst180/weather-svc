import asyncio

import json

from flask.json import jsonify
import weather

print("Hello!")

city = "Philadelphia"
loop = asyncio.get_event_loop()
current_weather = loop.run_until_complete(weather.getweather(city))

print(jsonify({
    'city': city,
    'current_temp': current_weather.current.temperature,
    'feels_like': current_weather.current.feels_like,
  }))