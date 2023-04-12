import requests
#ua user agent ua伪装

url = "https://www.sogou.com/web?"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

kw = input('Enter a word: ')
param = {
    'query' : kw
}
response = requests.get(params= param, url = url, headers = headers)
page_text = response.text
fileName = kw + '.html'
with open(file = fileName, mode = 'w', encoding = 'utf-8') as fp:
    fp.write(page_text)
print(f"{fileName}保存成功！ ")