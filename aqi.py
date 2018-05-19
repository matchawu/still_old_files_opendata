import json
import demjson

config = json.loads(open('json/aqi.json').read())
json = demjson.encode(config)
print (json)

# config["AQI"]
# config["County"]