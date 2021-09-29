import json
from signup import *
def log():
    file=open("signup.json","r")
    c=json.load(file)
    user_id=(input("enter your Email id:- "))
    user_password=(input("enter your password:- "))
    if user_id==c['Emailid']:
        if user_password==c["password"]:
            print("login done ")
        else:
            print("your password is rong plese try again")
    else:
        print("incorect mail id plese check")
        js_file()
