---
layout: page
title: College Free T-Shirt Emailer  
description: A Python Projects I worked on to learn more about programming and for fun early on in my college career 
img: assets/img/excel-python.webp
importance: 3
category: fun
---


<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/programmer-screen.jpeg" title="code" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>


#### [GitHub Repo](https://github.com/ColeFeely6/Independent-Python-Projects/tree/main/college-free-tshirt-emailer)


## Introduction


The Summer of 2020, my sister showed me a TikTok where kids were asking colleges for free t-shirts, saying they were a student looking to apply and wanted to rep the school and in return, got some free t-shirts! I found this very interesting, so I decided to put my introduction to programming skills to use. I would use a python script to take data from a spreadsheet from all schools in the US and the emails of all the recruitment offices from those schools, then email them inquiring about a free t-shirt. Out of 2,000 schools, surely a few would send one! And indeed they did, I got 5 free t-shirts! It would be interesting to perform this experiment again now that the trend has died down, it seems the schools caught on pretty quick at the time. 

## Building


<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/excel-python.webp" title="excel python" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>

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
