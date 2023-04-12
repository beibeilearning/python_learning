name = "黑马程序员"
print(type(name))

name = 'developer'
print(type(name))

name = """
黑马程序员
"""
print(type(name))

print(' "黑马程序员" ')
print(" '黑马程序员' ")
print("\"黑马程序员\"" )
print(  ' \' hello \' ' )

tel = 555555
name = "666"
print(name + "hello" + "bird" + name + str(tel))

a = "hello"
b = "world"
num = 3198329829
print("hahahahahah%s" %a)
print("ad%ss, jdias%ssss" % (num,num))

name = "companey"
year = 2020
price = 19.99

message = "%s, build at %d, price is %.2f" % (name, year, price)
print(message)

num1 = 19.23321
num2 = 13

print("宽度为20，精度为3， return：%20.3f"% num1)
print("宽度为10，精度为1， return：%10.1f"% num1)