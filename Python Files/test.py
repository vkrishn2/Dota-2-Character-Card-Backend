import requests
import json
import sys
from os import path


response = requests.get("http://www.dota2.com/datafeed/herodata?language=english&hero_id=16").text

print(response)
