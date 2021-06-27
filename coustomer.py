#coustomer

import time
import sqlite3
import os
import sys


connection = sqlite3.connect('coustomer.db')
c = connection.cursor()


try:
    c.execute('CREATE TABLE coustomer(code INT(5) PRIMARY KEY, name varchar(20), phone_no VARCHAR(15), amount_spent INT(5), location VARCHAR(40), amount_on_account INT(5), prime INT(1))')
    connection.commit()
    #code, name, phone_no, amount_spent, location, amount_on_account, prime
except:
    pass


def new():
    try:
        c.execute('SELECT count(*) FROM coustomer')
        code = int((str(c.fetchall()))[2])
        name = input('name : ')
        phone_no = input('phone no. : ')
        amount_spent = str(0)
        location =  input('location : ')
        amount_on_account = input('amount on account (if any) : ')
        prime = input('prime member : ')
        sep = ','
        _ = '\''
        q = 'INSERT INTO coustomer VALUES(' + str(code) + sep + _ + name + _ + sep + _ + phone_no + _ + sep + amount_spent + sep + _ + location + _ + sep + amount_on_account + sep + prime + ')'
        c.execute(q)
        connection.commit()
    except:
        print('error')
        new()
    

def see_all_data():
    c.execute('SELECT * FROM coustomer')
    print('(code, name, phone_no, amount_spent, location, amount_on_account, prime)')
    for i in c.fetchall():
        print(i)
    input('')






def return_sno_from_phone_no(phone_no):
    c.execute('SELECT * FROM coustomer')
    content = c.fetchall()
    for i in content:
        if phone_no == i[2]:
            return i[0]