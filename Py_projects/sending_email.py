# this module creates the object to send the email to the reciver
import smtplib
#this module open and read the file
import csv
#this will substitute the values to the place holders
from string import Template
# It takes the message and attachments
from email.mime.multipart import MIMEMultipart
# it creates the object and set the text to pass as an argument to the mimemultipart
from email.mime.text import MIMEText


# below function reads the txt file and retuns as Template format
#from adodbapi.examples.xls_read import row


def read_template(filename):
    with open("C:\\Users\\yjasw\\OneDrive\\Documents\\HTML\\template.txt",'r',encoding='utf-8') as temp_file:
        temp_file_content = temp_file.read()
        return Template(temp_file_content)


# Now configure the SMTP server
username=str(input("Enter your Email address :"))
password=str(input("Enter your Password :"))

s=smtplib.SMTP(host="smtp.gmail.com",port=587)
s.starttls() #Puts the connection to the SMTP server into TLS mode
s.login(username,password)

# passing the txt file to read_template function
message_template=read_template('template.txt')

#now read the csv_file
with open("C:\\Users\\yjasw\\OneDrive\\Documents\\HTML\\details.csv",'r') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')

    # below line skip the first row(headers)
    next(csv_reader)

    for row in csv_reader:
        msg = MIMEMultipart()  # create a message
        # add in the actual person name to the message template
        message=message_template.substitute(PERSON_NAME=row[0],MATH=row[2],ENG=row[3],SCI=row[4])
        print(message)

        # setup the parameters of the message
        msg['FROM']=username
        msg['TO']=row[1]
        msg['SUBJECT']='final grades'

        # add in the message body
        msg.attach(MIMEText(message,'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
s.quit()


