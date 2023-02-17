---
layout: page
title: Independent Python Projects  
description: Python Projects I made on my own to learn more about programming and for fun early on in my college career 
img: assets/img/python.png
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

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/excel-python.webp" title="excel python" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>


<a href="https://github.com/ColeFeely6/Independent-Python-Projects">GitHub Repository</a>

## College Free T-Shirt Emailer

<a href="https://github.com/ColeFeely6/Independent-Python-Projects/tree/main/college-free-tshirt-emailer">Free T-shirt Emailer Folder</a>

As you may know from my digital independence post, I am not on TikTok, but in the summer of 2020, my sister was. Apparently there was a trend going around where kids were asking colleges for free t-shirts, saying they were a student looking to apply and wanted to rep the school. I found this very interesting, so I decided to use my introduction to programming skills to use. I would use a python script to take data from a spreadsheet from all schools in the united states and the emails of all the recruitment offices and email them inquiring about a free t-shirt. Out of 2,000 schools, surely a few would send one! And indeed they did, I received a lot of denials but also a 5 free t-shirts! It would be interesting to perform this experiment again now that the trend has died down. 

First thing was to find a spreadsheet online of the college names and their recruiting office's email address. Then, the first scipt was made to parse through that spreadsheet and create two arrays: one for the names of the schools 'names' and one for the emails 'emails'. This file ws called speadsheet_python.py:

#### spreadsheet_python.py

{% highlight python linenos %}

import xlrd

path = "College Emails.xlsx"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

names = []
emails = []

for i in range(1,inputWorksheet.nrows):
    names.append(inputWorksheet.cell_value(i,0))
    emails.append(inputWorksheet.cell_value(i,1))

{% endhighlight %}

Once all the names and emails are all stored in those variables, we will write another script to send out all those emails.

#### emailer_python.py

{% highlight python linenos %}

import smtplib
import spreadsheet_python as sp
#import testspreadsheet_python as ts


my_email = 'your@email.com'
my_password = ''

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(my_email,my_password)
    


    
    
    
    for i in range(0,len(sp.names)):
        print(sp.names[i],i)
        print(sp.emails[i])
        subject = 'Consider attending in the spring'
        body = 'Dear Office of Admissions, (Message asking for T-Shirt) (Address) (Sincerely, Name)'%sp.names[i]
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(my_email,sp.emails[i],msg)

{% endhighlight %}

This code uses the smtplib library to send emails automatically from your email account. From here, we can set up a loop to run through all those emails and send them out automatically so we don't have to do it manually. First we import 'smtplib' and out 'spreadsheet_python' script that our lists of emails and names. Then we set up and log into our email through smtplib. The we iterate through our list of names and print the current name and email to the terminal. We create a variable subject that is a string that will be placed in the subject of the email. Next we write a general email where we can automatically insert the name of the University into the string. Finally, we put all those pieces together and send the email!

#### Other notes on the GitHub

I used some test spreadsheets first before using the real thing, those can be found within the folder as well under 'emailtest.xlsx' and 'testspreadsheet_python.py'. 

## Amazon Robot

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/web-scraping.png" title="web scraping" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>

<a href="https://github.com/ColeFeely6/Independent-Python-Projects"></a>

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



