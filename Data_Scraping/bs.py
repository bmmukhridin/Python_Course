from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-gv-r9060xtgaming-oc-16gd-radeon-rx-9060-xt-16gb-graphics-card-triple-fans/p/N82E16814932806"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

price = doc.find(class_="price-current").get_text().strip()
print(price)