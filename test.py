import urllib3
import json
import requests

http = urllib3.PoolManager()

url = 'http://opendata2.epa.gov.tw/AQI.json'
response = http.request('GET', url)
content = json.loads(response.data.decode('utf-8'))  

for x in range(91):
    print(content[x]['SiteName']+' has AQI : '+content[x]['AQI']+' at '+content[x]['PublishTime'])
    print('It seems that air in this site is '+ content[x]['Status'])
    print('\n')
