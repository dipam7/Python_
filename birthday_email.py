import datetime
import smtplib

# edit this variable to change the text file to be used
BIRTHDAY_FILE = 'birthdays.txt'
MONTHS = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

# makes a dictionary of all birthdays
# months are stored as keys
# the value of the keys is a list of tuples
# where each tuple consists of the person's
# birthdate, name and email address
birthdays_dict = {}
temp_month = ''

# read the contents of the file
fw = open(BIRTHDAY_FILE, 'r')
file_contents = fw.read()
file_contents = file_contents.split('\n')


def sort_birthdays():
	for element in file_contents:
		# ignore whitespace
		if element == '':
			continue
	
		# if the month is seen for the first time
		# initialise the month as a key
		if element.upper() in MONTHS:
			temp_month = element
			birthdays_dict[element] = []
	
		# else add the date, person's name and email
		# in the month's list of tuples
		else:
			# split the string at ':'
			# and strip the string of whitespaces
			my_tuple = [x.strip() for x in element.split(':')]
			birthdays_dict[temp_month].append(tuple(my_tuple)) 
		

def check_for_birthday():
	now = datetime.datetime.now()
	current_month = MONTHS[now.month - 1]
	current_day = now.day

	print('The current month is ' + current_month)

	# list of everyone who has a birthday this month
	birthdays_in_current_month = birthdays_dict[current_month.title()]
	# print('The following people have birthdays this month ' + str(birthdays_in_current_month))

	has_birthday = 0
	# find if anyone has a birthday today
	for element in birthdays_in_current_month:
		if(int(element[0]) == current_day):
			birthday_person = element[1]
			birthday_person_email = element[2]
			send_email(birthday_person, birthday_person_email)
			#print('Today\'s date is ' + element[0] + 'th' + ' ' + current_month)
			#print(element[1].upper() + '!!!!!!!' + ' has a birthday today')
			#print('Email him/her on ' + element[2])
			has_birthday = 1
			
	if has_birthday == 0:
		print('Nobody was born today :( ')
		print('Try again, tomorrow')
		
def send_email(name, email):
	fromaddr = 'user@gmail.com' 
	toaddrs  = email
	msg = "\r\n".join([
	  "From: user@gmail.com",
	  "Subject: Just a message",
	  "",
	  "Dear, " + name + "\nYour message here"
	  
	  ])
	username = 'user@gmail.com'
	password = 'pwd'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
		

		
sort_birthdays()
check_for_birthday()	

# check the complete dict
# print(birthdays_dict)
