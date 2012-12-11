#! /usr/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pycurl
import StringIO
import os



def mailme():

	to = 'recepiant@somedomain.com'
	gmail_user = 'youremail@gmail.com'
	gmail_pwd = 'password'

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Subject:Results S3!"
	msg['From'] = gmail_user
	msg['To'] = to
	text = "S3 Results Published !"
	html = s

	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')


	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	msg.attach(part1)
	msg.attach(part2)

	smtpserver.sendmail(gmail_user, to, msg.as_string())
	print 'done!'
	smtpserver.close()




buff = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://202.88.252.18/Revaluation/revaluation_memo2.php')
c.setopt(c.POSTFIELDS,'revid=7&regno=ctahecs006&dobd=17&dobm=6&doby=1989&gosub=GO')
c.setopt(c.WRITEFUNCTION,buff.write)
c.perform()




s=buff.getvalue()

slug=len(s)

if(slug!=255):

		if(os.path.isfile("temp1")==True):
			print("Already Mailed !")
		else:
			mailme()
			os.system("touch temp1")
else:
	print("Nothing Yet")


buff.close()


