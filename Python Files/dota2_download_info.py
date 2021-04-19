import requests
import json
import sys
from os import path
import time
import re

def get_info():
    response = json.loads(requests.get("https://www.dota2.com/datafeed/herolist?language=english").text)

    numheroes = len(response['result']['data']['heroes'])
    print("The number of heroes in Dota 2: ",numheroes)

    id_dict = {value['id']:value['name_english_loc'] for value in response['result']['data']['heroes']}
    #print("DEBUG id_dict: ", id_dict)

    with open('herolist.json','w') as f1:
        json.dump(response, f1)


    count = 0
    with open('heroes.json','w') as f:
        f.write('[')
        for id_val,name in id_dict.items():
            count += 1 
            time.sleep(5)
            response2 = json.loads(requests.get("http://www.dota2.com/datafeed/herodata?language=english&hero_id="+str(id_val)).text)
            if count != numheroes:
                f.write(',')
        json.dump(val1, f)
        f.write(']')


print("Requesting and downloading information from API...")
print("First checking for previous files...")
if path.exists("herolist.json"):
    print("herolist.json has already been created.")
    herolistcheck = True
else:
    print("herolist.json has not been created.")
    herolistcheck = False
    
if path.exists("heroes.json"):
    print("heroes.json has already been created.")
    heroescheck = True
else:
    print("herolist.json has not been created.")
    heroescheck = False

if heroescheck and herolistcheck:
    print("Both files have been created.")
    if len(sys.argv) == 2 and sys.argv[1] == "UPDATE":
        print("Overriding. UPDATE Protocol initiated.")
        get_info()
    
else:
    print("Both files have not been created. Creating now.")
    get_info()



