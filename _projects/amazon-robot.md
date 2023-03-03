---
layout: page
title: Amazon Robot  
description: Python Projects I made on my own to learn more about programming and for fun early on in my college career 
img: assets/img/api.jpeg
importance: 1
category: fun
---


<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/programmer-screen.jpeg" title="code" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>


# The Projects



<a href="https://github.com/ColeFeely6/Independent-Python-Projects">GitHub Repository</a>


<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/web-scraping.png" title="web scraping" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>


This project was an endevour to understand more about how Web APIs work and to use python to interact with them. To do this, I wrote a script that gets information on a product from the Amazon Website. 

{% highlight python linenos %}

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
    

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')
title = soup.find("span",id='productTitle').get_text()
price = soup.find("span",id="priceblock_ourprice")
print(price)
print(title.strip())

{% endhighlight %}

This code is an example of web scraping using the requests and BeautifulSoup libraries in Python. At this point in time, I was interested in the changes to the price of certain weightlifting equipment, hence I evaluated the CAP Beast Barbell, but any Amazon product would suffice. 

The script sends a GET request to an Amazon product page using the requests module and retrieves the HTML response. Then it uses the BeautifulSoup library to parse the HTML content of the page and extract the product title.

The script defines a function getPrice that does the above mentioned tasks, and prints the type of the title variable.

the last part of the code is an example of how to extract the price of the product from the same Amazon page using BeautifulSoup, but it is not actually used in the final script.



