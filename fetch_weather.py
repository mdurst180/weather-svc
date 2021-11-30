import asyncio

import json
import weather

print("Hello!")

city = "Philadelphia"
loop = asyncio.get_event_loop()
current_weather = loop.run_until_complete(weather.getweather(city))