# 多条件判断， 判断互斥有顺序
# height = int(input("What is your height?"))
# vip_level = int(input("What is your vip level? "))
#
# if (height < 120):
#     print("Your height is lower than 120 cm, ticket for free")
#
# elif (vip_level > 3):
#     print("Your vip level greater than 3. You get free ticket")
#
# else:
#     print("You have to buy a ticket")

# import random
# num = random.randint(1,10)
#
# # 1st guess
# guess_num = int(input("guess the number: "))
# if guess_num == num:
#     print("congratulation! You got it!")
# else:
#     if guess_num < num:
#         print("too small")
#     else:
#         print("too big")
#
#     # 2ed guess
#     guess_num = int(input("2ed guess!"))
#     if guess_num == num:
#         print("congratulation! You got it in 2ed guess!")
#     else:
#         if guess_num < num:
#             print("too small")
#         else:
#             print("too big")
#
#         # 3rd guess
#         guess_num = int(input("3rd guess!"))
#         if guess_num == num:
#             print("congratulation! You got it in 2ed guess!")
#
#         else:
#             if guess_num == num:
#                 print("congratulation! You got it in 3rd guess!")
#             else:
#                 print("You use up all the opportunities!")
#
# print(f"Actual number is {num}")

# i = 10
# while i < 20:
#     print(f"第{i-9}次打印：世界第一甜，华悦李泽言！")
#     i += 1
#
# sum = 0
# i = 1
# while i <= 100:
#     i += 1
#     sum += i
# print("Sum is %d" % sum)

# import random
# num = random.randint(1,100)
# flag = True
# count = 0
# while flag:
#     guess_num = int(input("Guess the number here: "))
#     count += 1
#     # get the right num
#     if guess_num == num:
#         print("Congratulation! ")
#         flag = False
#     else:
#         if guess_num > num:
#             print("Number is too big")
#         else:
#             print("too small")
#     print(f"This is the {count} time")

#
# import random
# i = 1
# while i <= random.randint(1,100):
#     print(f"Today is day {i}")
#     j = 0
#     while (j < 10):
#         print(f"送给小美的第{j}朵玫瑰花")
#         j += 1
#     print("I love you MEI")
#     print("*******************************")
#     i += 1
#
# print(f"Day {i-1}, succeed!")

# print("beibei", end='')
# print("cute", end='')
# print("\n*******************************")
#
# print("hello\tworld")
# print("happy\teveryday")

i = 1

while i <= 9:
    # the number of column in current row
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i += 1
    print()
