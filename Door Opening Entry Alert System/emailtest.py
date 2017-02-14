import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

def sendemail():
    msg = MIMEMultipart()
    msg['Subject'] = 'Email python test'
    msg['From'] = 'Sender Email Address'
    msg['To'] = 'Recipients Email Address'
    msg.preamble = 'Motion detected'
    fp = open("plaintext.txt", 'rb')
    text = MIMEText(fp.read())
    fp.close()
    msg.attach(text)
    fp = open("test.png", 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.live.com', 587)
    s.ehlo()
    s.starttls()
    s.login('Sender Email Address Username, 'Sender Email Address Password')
    s.sendmail('Sender Email Address, ['Recipients Email Address'], msg.as_string())
    print "email sent"
    s.quit()
