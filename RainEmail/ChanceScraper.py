import requests
from bs4 import BeautifulSoup
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Soup():
    page = requests.get('***************')  #Enter the URL of your local weather from weather.com on the 10 day forcast page
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def ChanceOfRain(Text):
    Chance = []
    for body in Text.findAll('td'):
        Chance.append(body.text)
    Chance = Chance[4]
    return Chance

def SendEmail():
    #Send the email to say that it's going to rain
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('**************', '******************')

    # add in the actual person name to the message template
    message = 'Its going to rain'
    # Prints out the message body for our sake
    msg = MIMEMultipart()
    # setup the parameters of the message
    msg['From']='*****************'
    msg['To']='***************'
    msg['Subject']="RAIN"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()
    print('Sleeping')
    time.sleep(86400)

def SendEmailDecision(Percp):
    if int(Percp[0]) >= 5:
        SendEmail()
    else:
        print('No Rain')

def main():
    Percent = ChanceOfRain(Soup())
    SendEmailDecision(Percent)

if __name__ == "__main__":
    # calling main function
    main()
