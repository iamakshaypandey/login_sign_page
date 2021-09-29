import json
from login import *
def js_file():
    print("wel-come to sign-up page:-")
    print("plese enter your details:- ")
    data2={}
    name=input("enter your name:- ")
    Emailid=input("enter your mail id:- ")
    dateofbirth=input("enter your date of birth:- ")
    password=input("enter you password:- ")
    data2["name"]=name
    data2["Emailid"]=Emailid
    data2["data of birth"]=dateofbirth
    data2["password"]=password
    # print(data2)
    file=open("signup.json","w")
    json.dump(data2,file,indent=4)
    print("done")
    file.close()
    