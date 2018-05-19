import json

with open('ex.json' , 'r') as reader:
    jf = json.loads(reader.read())

print(jf['data']['hi_info']['login_ip'])