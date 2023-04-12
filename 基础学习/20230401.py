import requests

url = 'https://www.baidu.com'
response = requests.get(url)

print('Response Status Code:', response.status_code)
print('Response Content:', response.content.decode())


name = input("tell me who you are?")
print("Ok, I know you are %s" % name)

num1 = input("电话号码？")
num1_toInt = int(num1)
name = input("name is what? ")
print(f"ok, your number is: {num1_toInt}, name is {name}")