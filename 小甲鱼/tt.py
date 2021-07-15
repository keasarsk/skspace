import urllib.request
import os
page=100
# url='http://setu69.buzz/?201970.html'
url='http://kkoo.icu/1490.html'

response = urllib.request.urlopen(url)
html = response.read()
print(html)
# while page <= 115:
#     print(page)
#     response = urllib.request.urlopen(url)
#     html = response.read()
#     page +=1
#     pass