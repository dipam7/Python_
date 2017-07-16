#! /usr/bin/python

import notify2
import random
from time import sleep

# this variable is in seconds.
TIME_BETWEEN_WORDS = 300
# edit the variable below for using your own files
WORDS_FILE = 'week1.txt'


fw = open(WORDS_FILE, 'r')
file_contents = fw.read()
file_contents = file_contents.split('\n')


def sendmessage(word,meaning):
    notify2.init("Test")
    notice = notify2.Notification(word, meaning)
    notice.show()
    return

while True:
	i = random.randint(0,len(file_contents)-1)
	if i % 2 == 0:
		sendmessage(file_contents[i], file_contents[i+1])
		sleep(TIME_BETWEEN_WORDS)
		
	
