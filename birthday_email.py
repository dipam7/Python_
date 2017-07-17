import datetime

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
		
		
# check the complete dict
print(birthdays_dict)

now = datetime.datetime.now()
current_month = MONTHS[now.month - 1]
current_day = now.day


print()
print()
print()


print('The current month is ' + current_month)

# list of everyone who has a birthday this month
birthdays_in_current_month = birthdays_dict[current_month.title()]
# print('The following people have birthdays this month ' + str(birthdays_in_current_month))

# find if anyone has a birthday today
for element in birthdays_in_current_month:
	if(int(element[0]) == current_day):
		print('Today\'s date is ' + element[0] + 'th' + ' ' + current_month)
		print(element[1].upper() + '!!!!!!!' + ' has a birthday today')
		print('Email him/her on ' + element[2])
