import requests
from bs4 import BeautifulSoup


url = "https://www.amazon.com/CAP-Barbell-Beast-7-Foot-Olympic/dp/B006R4EOWI/ref=sr_1_4?dchild=1&keywords=barebell&qid=1589492066&sr=8-4&th=1"
goal_price = 150
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def getPrice():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    soup.encode('utf-8')
    title = soup.find('span',id="productTitle").get_text().strip()
    if title is None:
        title = soup.find('span',id="productTitle").get_text().strip()
    
    print(type(title))
    
if __name__ == "__main__":
    getPrice()
    

"""page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
title = soup.find("span",id='productTitle').get_text()

price = soup.find("span",id="priceblock_ourprice")


print(price)
print(title.strip())"""









