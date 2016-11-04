#!/usr/bin/env python2.7

#This file sends an email from the gmail account.
#Phase 1- send the email from one account to the other account
#Phase 2- Read the input from the user and use that for sending the email including the content.
#Phase 3- Read the input from the excel sheet, read the name, and send a personalized email to that#email id.
#Phase 4- Read multiple lines of input from the file and send the email.
#Phase 5- Add the GUI to the program.
#Enhancement- Dont display the password in the raw format while entering at the terminal.
#Phase 7- Send text messages as well.

from smtplib import *



print "Connecting to Gmail server. Please wait"
mysmtp= SMTP("smtp.gmail.com", 587)
res= mysmtp.starttls()
if(res[0] != 220):
	print "Connection failed. Please run again\n"
res= mysmtp.ehlo()
if(res[0] != 250):
	print "Connection to the gmail server failed. Please run again\n"
while 1:
	email= raw_input("Enter your email ID: ")
	password = raw_input("\nEnter your password: ")
	
	res= mysmtp.login(email, password)
	if(res[0] == 235):
		print "Login successful\n"
		break
	else:
		print "Login details are wrong. Please enter again\n"

rep_email= raw_input("Enter the receipients email ID: ")

#PARAS- Add the reg expression to check if the email is in proper syntax

#PARAS- Resolve the subject issue.
mysmtp.sendmail(email, rep_email, "Subject: Test Email.\n This is a test email from my program")

