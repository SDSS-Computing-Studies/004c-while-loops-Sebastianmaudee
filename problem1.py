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

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
u = input("Enter username: ")
t = 0
while u !="admin": 
    print("Access denied")
    t = t + 1
    u = input("Enter username: ")
    if t == 2:
        print("Too many failed attempts. Access denied.")
        break
while u == "admin":
    p = input("Enter password: ")
    if p != "1234":
        t = t + 1
        print("Access denied")
    if t == 3:
        print("Too many failed attempts. Access denied.")
        break
    if p == "1234":
        print("Access granted")
        break
