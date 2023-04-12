import requests
url = "https://www.sogou.com/"
response = requests.get(url = url)
page_text = response.text
print(page_text)

with open('./sogou.html', mode = 'w', encoding="utf-8") as fp:
    fp.write(page_text)

print("爬取数据结束")

# 简易网页采集器