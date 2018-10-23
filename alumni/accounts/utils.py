
# Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_mail(username,password,email):
	  
	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	  
	# start TLS for security 
	s.ehlo()
# email_conn.starttls()
	s.starttls() 
	  
	# Authentication 
	try:
		s.login("tusharsetia7@gmail.com","rajputanamaha1" ) 
	except Exception as e:
		# print(e)
		pass
	  
	# message to be sent 
	# message = "username : {} \npassword : {}".format(username,password)
	# # message = "Hello "
	# print("%%$$%$%$%$%$")
	# print(message)
	  
	# # sending the mail 
	# s.sendmail("tusharsetia7@gmail.com", email, message) 

	msg=MIMEMultipart("alternative")
	msg["Subject"]="Credential"
	msg["From"]="tusharsetia7@gmail.com"	

	

	html_txt= """\
	          <html>
	             <head></head>
	             <body><p>username : <br>"""+username+"""</p><br><p>password : <br>"""+password+"""</p></body>
	          </html>
	          """

	p2=MIMEText(html_txt,"html")
	msg.attach(p2)


	s.sendmail("tusharsetia7@gmail.com",email,msg.as_string())
	  
	# terminating the session 
	s.quit() 
