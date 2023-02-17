import smtplib
import spreadsheet_python as sp
#import testspreadsheet_python as ts


my_email = 'colehfeely@gmail.com'
my_password = 'Sonictine@393'

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(my_email,my_password)
    

    '''subject = 'Consider attending in the spring'
    body = 'Dear Office of Admissions, \n\n Due to the recent pandemic, my family must hold off from sending me to college this fall. I was considering attending %s in the spring for the beautiful campus and great student life! I would still love to show my support for the school but I have not gotten the chance to visit campus and buy apparel. I would love it if you could send me T- shirt if you could! I am a size medium and my address is: \n Cole Feely \n 393 Lebanon Street \n Melrose, MA 02176 \n Thank you so much and hopefully I will be on campus in the spring, \n Cole Feely'%'UMass'
    
    
    
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(my_email,'colehfeely@gmail.com',msg)
    #for i in range(len(sp.names)):
     #   smtp.sendmail(my_email,str(sp.emails[i]),msg)'''
    
    
    
    for i in range(1632,len(sp.names)):
        print(sp.names[i],i)
        print(sp.emails[i])
        subject = 'Consider attending in the spring'
        body = 'Dear Office of Admissions, \n\n Due to the recent pandemic, my family must hold off from sending me to college this fall. I was considering attending %s in the spring for the beautiful campus and great student life! I would still love to show my support for the school but I have not gotten the chance to visit campus and buy apparel. I would love it if you could send me T- shirt if you could! I am a size medium and my address is: \n Cole Feely \n 393 Lebanon Street \n Melrose, MA 02176 \n Thank you so much and hopefully I will be on campus in the spring, \n Cole Feely'%sp.names[i]
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(my_email,sp.emails[i],msg)