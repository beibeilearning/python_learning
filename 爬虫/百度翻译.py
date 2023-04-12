import requests
import json
post_url = "https://fanyi.baidu.com/sug"

word = input("Enter a keyword: ")
data = {
    'kw' : word
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

}
response = requests.post(url = post_url, data = data, headers=headers)
dic_obj = response.json()
print(dic_obj)

file_name = "./" + word + ".json"
fp = open(file_name, 'w', encoding='utf-8')
json.dump(obj = dic_obj, fp = fp, ensure_ascii=False)
print("over")