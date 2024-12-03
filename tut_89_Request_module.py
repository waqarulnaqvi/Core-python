"NO NEED KNOW LEARN IT LATTER"
# 2 20
# first install request module.
# pip install requests
# import requests
# from bs4 import BeautifulSoup
# response=requests.get("https://www.google.com")
# response=requests.get("https://www.codewithharry.com")
# print(response.text)
# url="https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r=requests.get(url)
# # print(r.text)
#
#
# soup=BeautifulSoup(r.text,'html.parser')
# print(soup.prettify)
# data={
#     "title":"harry",
#     "body":"bhai",
#     "userId":12,
# }
# headers={
#     'Content-type':"application/json; charset=UTF-8",
# }
# url="https://jsonplaceholder.typicode.com/posts"
# response=requests.post(url,headers=headers,json=data)
# print(response.text)