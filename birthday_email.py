import datetime

BIRTHDAY_FILE = 'birthdays.txt' 
MONTHS = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

birthdays_dict = {}
current_month = ''

fw = open(BIRTHDAY_FILE, 'r')
file_contents = fw.read()
file_contents = file_contents.split('\n')

for element in file_contents:
	# ignore whitespace
	if element == '':
		continue
	
	# if the month is seen for the first time
	# initialise the month
	if element.upper() in MONTHS:
		current_month = element
		birthdays_dict[element] = []
	
	# else add the date and person's name
	# in the current month's list
	else:
		birthdays_dict[current_month].append(element) 
		
		# print(birthdays_dict[current_month][0][:2])
		
print(birthdays_dict)

now = datetime.datetime.now()

# prints the current month
# print(now.month)
