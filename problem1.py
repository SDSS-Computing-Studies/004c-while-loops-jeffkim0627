##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""

usrname = str(input("Enter a usename"))
passwrd = str(input("Enter a password"))
count = 0


while ((usrname != "admin") or (passwrd != "12345")) or count < 3:
    count = count + 1
    print("Access denied")
if (usrname == "admin") and (passwrd == "12345"):
    print("Access granted")