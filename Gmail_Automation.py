#Gmail Automation
#By : github.com/thesaahilraj

'''
A simple Automation code used to Send Email using Gmail smtp
'''


#import smtp Library
import smtplib

#create an Object
conn = smtplib.SMTP("smtp.gmail.com")
conn.ehlo()
conn.starttls()

#Login with the Senders Email Address
conn.login("sendersemail@gmail.com","password123")

#Send Mail
# obj.send("sender's mail", "Receiver's Mail" , "Message")
conn.send("sendersemail@gmail.com", "thesaahilraj@gmail.com" ,"Subject: Automation \n\n Body: This mail is Sent using gmail Automation")
