# Made by Rachit Master
# Web scraping project

# 1
import requests
url = "https://www.newegg.com/global/in-en/samsung-galaxy-z-flip-3-5g-6-7-black/p/N82E16875168090?Item=N82E16875168090"
page = requests.get(url)
print(page)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find_all('div', attrs={"class":"price-current"})[0].get_text()
print(price)

#2
if price<₹ 100,000:
    print("Price is lower then 100,000!")
