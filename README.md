# Simple-Encryption-Program
A simple Python program that encrypts/decrypts whatever message you input. This is a little difficult if you're a beginner but if you're up for a challenge, this is the a really good mini program to make. 

# How does this work?
So you ask the user whether or not you want to decrypt or encrypt a message, then you input the message you want to encrypt/decrypt. There are many different ways you can encrypt a message, but to make this easy for beginners, I made it so that whenever you encrypt a message, it replaces whatever character there is with another value. For example: if you encrypt the word, "Hello," it may replace it with "4$;;2" And this will not change, so the letter, 'l' will always be ";". However everytime you run a program, it will be randomized. So the letter 'l' may not be ';'.

# How to run the program?
To play, make sure you have python 3+ installed, then you need to download the main.py file and place it anywhere in your computer. Then, go to your cmd (terminal for mac or linux users) and then navigate to the folder path using "cd [insert folder name here, dont include the brackets]. Once you are in the folder where the main.py file is stored, run the py file by typing, "python main.py."

# HINTS:
use the string and random module if you want to know how to get all the different types of characters, rather than inputing them yourself manually.
to randomize the key, convert the characters from the string module to a list. list(string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.whitespace)
