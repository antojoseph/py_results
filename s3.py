#! /usr/bin/python
import pycurl
import StringIO
import os




def save_result(s):
		with open("result.html","w") as fp:
				fp.write(s)
		fp.close()			


def mailme():
	import smtplib
	to = 'recepiant@somedomain.com'
	gmail_user = 'youremail@gmail.com'
	gmail_pwd = 'password'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Results S3! \n'
	print header
	msg = header + '\n Dude , University Results Just pulished for S3 Revaluation.. check it ! \n\n'
	smtpserver.sendmail(gmail_user, to, msg)
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
			save_result(s)
			mailme()
			os.system("touch temp1")


buff.close()


