import os
import math
import smtplib
import random
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
digits = '0123456789'

OTP = ""

for i in range(6):
    OTP +=digits[math.floor(random.random()*10)]
message = OTP + " is your otp"
#print(message)

username=str(input("Enter your Email Address :"))
password=str(input("Enter your password :"))

s=smtplib.SMTP(host="smtp.gmail.com",port=587)
s.starttls()
s.login(username,password)
def email_check():
    while True:
        try:
            email_id=input("Enter your Email ID:")
            if(re.fullmatch(regex, email_id)):
                return email_id
        except smtplib.SMTPRecipientsRefused:
            print("Invalid Email")


#email_id=input("Enter your Email ID:")
s.sendmail('&&&&&&&',email_check(),message)
s.quit()
a=input("Enter your OTP:")
if a == OTP:
    print("You your email address is verified")
else:
    print("Please Check your OTP again")

# s.starttls()
# s.login(username, password)
# emailid = input("Enter your email: ")
# s.sendmail('&&&&&&&&&&&',emailid,message)
# a = input("Enter Your OTP >>: ")
# if a == OTP:
#     print("Verified")
# else:
#     print("Please Check your OTP again")
