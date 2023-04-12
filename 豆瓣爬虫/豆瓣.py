import requests
import json

url = "https://movie.douban.com/j/chart/top_list"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


param = {
    'type':' 24',
    'interval_id':' 100:90',
    'action':'',
    'start':' 1',
    'limit':' 20',
}

response = requests.get(url = url, params=param, headers=headers)
list_data = response.json()

fp = open("./douban.json", mode='w', encoding = 'utf-8')
json.dump( obj = list_data, fp=fp, ensure_ascii = False)
print("Success! ")