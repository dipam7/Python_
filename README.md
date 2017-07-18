# Python projects

These are some of the projects I've made while learning python.

## Vocabulary

This program takes a list of **words** with their **meanings** as input and regularly notifies you with a _random_ word from the list to help you better remember the words. (**NOTE**: Make sure the code and text files are in the same folder.) Files include:

- vocab.py
- Various text files in the vocab folder.


## Wikipedia crawler

**NOTE:** This code was written in python3.

According to a study, if you keep clicking on the first legit link (excluding pronounciation and other such links) of any Wikipedia article, you ultimately end up on the article about Philosophy. (ofcourse, you can go further)

This study elimates loops present in the pages. Files included are:
- wikipedia_crawler.py

## Birthday email program

This code reads a text file of birthdays, and sends that person a predefined general email about the same.

**Things to edit**:
- First of all insert all of your friend's details in the dummy_birthdays.txt
- Then change the filename from birthdays.txt to dummy_birthdays.txt in the birthday_email.py file.
- Then skip to the send_email() function in birthday_email.py and fill up the following:
 -- fromaddr
 -- Inside msg:
  --- From
  --- Subject
  --- Your message
 -- username (email)
 -- password

Files included:
- birthday_email.py
- dummy_birthdays.txt

#### Instructions for dummy_birthdays.txt
- It should contain Month followed by people's details on new lines as shown.
- Whitespaces are okay but seperating the details with ':' is essential.
- You can exclude month if nobody has a birthday in that month.
 
To run python code:
```
$python file_name.py
```

If you have installed multiple versions of python, then to run a code using python 3:
```
$python3 file_name.py
```

There are some more projects that I've made. They run on a tool called [Codeskulptor](http://www.codeskulptor.org/). Check them out in the links below.
  
[Guess the number](http://www.codeskulptor.org/#user41_qzaX97GhdVPzjO5_1.py)

[Pong - the game](http://www.codeskulptor.org/#user41_0Viwl5q2e2_2.py)

[Simple task manager](http://www.codeskulptor.org/#user41_HG3EujvYA5_0.py)

[Memory game](http://www.codeskulptor.org/#user41_idXXiTroIzZHL0h.py)
