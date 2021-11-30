
import os

import asyncio

import json

import weather

import send_txt

print("Hello!")

city = "Philadelphia"
loop = asyncio.get_event_loop()
current_weather = loop.run_until_complete(weather.getweather(city))

print({
    'city': city,
    'current_temp': current_weather.current.temperature,
    'feels_like': current_weather.current.feels_like,
  })




_num = "2156208067"
_carrier = "at&t"
_email = "mdurst180@gmail.com"
_pword = os.environ['MAIL']
_msg = "Dummy msg"
_subj = "Dummy subj"
coro = send_txt.send_txt(_num, _carrier, _email, _pword, _msg, _subj)
# _nums = {"999999999", "000000000"}
# coro = send_txts(_nums, _carrier, _email, _pword, _msg, _subj)
asyncio.run(coro)