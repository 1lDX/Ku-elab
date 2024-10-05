ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'
########
User = input("Username: ")
password = input("Password: ")

if User == ADMIN_USERNAME and password == ADMIN_PASSWORD:
 print("Welcome, admin.")
else :
 print("You are not admin.")