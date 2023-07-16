# birth_year = input("what year were you born? ")
# curent_year = 2022
# print(f"You are {2022 - (int(birth_year))}")

# user_name = input("What is your username? ")
# password1 = input("What is your password? ")

# password2 =len(str(password1))


# print(f"Hey {user_name} your password length is {password2 * '*'} ({password2})")


# basket = ['a', 'x', 'z', 'b', 'c', 'd', 'e', 'f']
# basket.sort()
# basket.reverse()


# print(basket[:  ])

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# counter = 0
# for i in my_list:
#     counter=  counter+ i
# print(counter)

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# for row in picture:
#     for pixel in row:
#         if (pixel == 0):
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print('')

# for i in range(len(picture)):
#     for j in range(len(picture[i])):
#         if picture[i][j] == 1:
#             picture[i][j] = "*"
#         else:
#             picture[i][j] = " "

# print(picture)


# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10


# def twoNumberSum(array, targetSum):
#     for x in array:
#         y = targetSum - x
#         print(x)
#         for y in array:
#             print(x)
#             if x+y == targetSum:
#                 return [x,y]
#     return []

# print(twoNumberSum(array, targetSum))

# def highestNumber(li):
#     number=[]
#     for i in li:
#         for j in li:
#             if i > j:
#                 number.append(i)
#     return max(number)


# OOP

# class PlayerCharacter:
#     def __init__(self, name):


# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f"took {t2-t1} s")
#         return result
#     return wrapper
#
#
# @performance
# def long_time():
#     for i in range(100000000):
#         i*5
#
# long_time()


import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select(".titleline")
votes = soup.select(".score")

def create_module_hn(links, votes):
    hn=[]
    for idx, item in enumerate(links):
        title =links[idx].getText()
        href = links[idx].get("href", None)
        hn.append({"title": title, "links": href})
    return hn
 
print(create_module_hn(links, votes))