import requests

url = "https://www.baidu.com/s?wd="
key_word = input("Enter a key word: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
params = {
    "query" : key_word
}


response = requests.get(url=url, params=params, headers=headers)
page_text = response.text
file_name = key_word + ".html"
with open(file = file_name, mode = 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(f"Save the file {file_name}! ")