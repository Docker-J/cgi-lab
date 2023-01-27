#!/usr/bin/env python3
import cgi
import cgitb
import os
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
from http.cookies import SimpleCookie
    
cgitb.enable()
form = cgi.FieldStorage()

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
username_cookie = cookie.get("username")
if(username_cookie):
    username_cookie = username_cookie.value

password_cookie = cookie.get("password")
if(password_cookie):
    password_cookie = password_cookie.value

if (username_cookie == username and password_cookie == password):
    print(secret_page(username_cookie, password_cookie))
else:
    username_entered = form.getfirst("username")
    password_entered = form.getfirst("password")

    if(not(username_entered == username and password_entered == password)):
        print(login_page())

    if(username_entered == username and password_entered == password):
        print(f"Set-Cookie:username={username}")
        print(f"Set-Cookie:password={password}")

        print(secret_page(username_entered, password_entered))
    elif(username_entered != None):
        print(after_login_incorrect())

# print("Username:", username)
# print("Password:", password)