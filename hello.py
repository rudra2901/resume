import json

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

fp = requests.get("https://www.flipkart.com/books/pr?sid=bks&q=cormen&otracker=categorytree")
content = fp.content
soup = BeautifulSoup(content, 'lxml')

#
# def scrape(x, y):
#     ret = []
#     l1 = soup.find_all(x, class_=y)
#     for j in range(len(l1)):
#         print(l1.__class__.'da.text)
#     len(ret)
#     return ret
#
#
# def scrape1(x, y):
#     ret = []
#     l1 = soup.find_all(x, herf_=y)
#     for j in range(len(l1)):
#         ret.append(l1[j].herf)
#     len(ret)
#     return ret


# desc = soup.find_all('a', class_='s1Q9rs')
# price = soup.find_all('div', class_='_30jeq3')
# author = soup.find_all('div', class_='_3Djpdu')
# rating = soup.find_all('div', class_='_4ddWXP')

# print(desc.text)
# at = scrape('a', 's1Q9rs')
pt = scrape('div', '_13oc-S')
# descriptions = scrape('div', '_3Djpdu')
# rt = scrape('div', '_4ddWXP')
# no_of_rating = scrape('div', '_2_RDZ')
# url = scrape1('a', 's1Q9rs')
# Create a list to store the descriptions
# for i in range(len(desc)):
#     descriptions.append(desc[i].text)
# len(descriptions)
# print(descriptions)

# for i in range(len(price)):
#     pt.append(price[i].text)
# len(pt)
# print(pt)

# for i in range(len(author)):
#     at.append(author[i].text)
# len(at)
# print(at)

# for i in range(len(rating)):
#     rt.append(rating[i].text)
# len(rt)
# print(rt)

# ds = {
    # 'Name': descriptions,
    # 'Price': pt,
    # 'Rating': rt,
    # 'No_of_rating': no_of_rating,
    # 'Author': pt,
    # 'u': url
# }
# print(json.dumps(ds, indent=2))

# print(soup.prettify())
# soup = BeautifulSoup(fp.text, 'html.parse')
# product = []
# prices = []
# product = soup.find('div', class_='s109rs')
# print(product.text)
