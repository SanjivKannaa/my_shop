#login
import time
import sqlite3
import os
import sys
import pyautogui


connection = sqlite3.connect('user_pass.db')
c = connection.cursor()

try:
    c.execute('CREATE TABLE users(name VARCHAR(20), username VARCHAR(20), password VARCHAR(15), admin VARCHAR(1))')
    connection.commit()
except:
    pass

def login():
    f = open('user.txt', 'r')
    c.execute('SELECT * FROM users')
    file_content = f.readlines()
    if len(file_content) > 0:
        for i in c.fetchall():
            if i[0] == file_content[0][:-1]:
                if i[3] == '1':
                    return 'admin'
                else:
                    return '0'
    username=input('username : ')
    password = input('password : ')
    r = ''
    c.execute('SELECT * FROM users')
    for i in c.fetchall():
        if i[1] == username:
            if i[2] == password:
                r = 'ok'
                f = open('user.txt', 'w')
                f.write(i[0] + '\n')
                if i[3] == '1':
                    f.write('admin')
                    return 'admin'
                else:
                    f.write('0')
                    return '0'
            else:
                r = 'wrong password'
                return False
    if r == '':
        r = 'no user found'
        return False

def new_user(name, username, password, admin):
    if admin in ['1', '0']:
        condition = True
    for i in c.fetchall():
        if username == i[1]:
            condition = False
            return 'username already exists'
    if condition :
        _ = '\''
        sep = ','
        q = 'INSERT INTO users VALUES(' + _ + name + _ + sep + _ + username + _ + sep + _ + password + _ + sep + _ + admin + _ + ')'
        print(q)
        time.sleep(1)
        c.execute(q)
        connection.commit()
        return True
    else:
        return False

def view_all_data(username, password):
    c.execute('SELECT * FROM users')
    auth = False
    for i in c.fetchall():
        if username == i[1]:
            if i[2] == password:
                if i[3] == '1':
                    auth = True
                else:
                    auth = False
                    return 'unauthorised access'
            else:
                auth = False
                return 'wrong password'
    if auth == True:
        c.execute('SELECT * FROM users')
        for i in c.fetchall():
            print(i)
        input('')
        return True
'''def login():
    username = input('username : ')
    password = input('password : ')
    c.execute('SELECT * FROM users')
    for i in c.fetchall():
        if i[1] == username and i[2] == password:
            return True
    return False'''

