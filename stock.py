#stock

import time
import sqlite3
import os
import pyautogui
import login
import stock
import coustomer


connection = sqlite3.connect('stock.db')
c = connection.cursor()

try:
    c.execute('CREATE TABLE stock(code VARCHAR(20) PRIMARY KEY, company VARCHAR(20), product VARCHAR(15))')
    c.execute('CREATE TABLE unique_stock(code VARCHAR(5), unique_code VARCHAR(5))')
    connection.commit()
    # stock => code (PK), company, product
    # uniqui_stock => code, uniqui_code, soldto
except:
    pass



def update_stock():
    if login.login() != 'admin':
        print('unauthorised access')
        time.sleep(1)
        update_stock()
    else:
        more = 'y'
        while more == 'y':
            code = input('code [5 digits] : ')
            quantity = int(input('new quantity : '))
            c.execute('select * from unique_stock')
            last_unique_code = 1
            for i in c.fetchall():
                if i[0] == code:
                    if int(i[1]) > last_unique_code:
                        last_unique_code = int(i[1])
            sep = ','
            _ = '\''
            for i in range(int(quantity)):
                q = 'INSERT INTO unique_stock VALUES(' + _ + code + _ + sep + _ +  str('0'*(5-len(str(last_unique_code+i+1))))+str(last_unique_code+i+1) + _ + ')'
                print(q)############################
                c.execute(q)
                connection.commit()
            if input('stop?(y) : ') == 'y':
                more = 'y'



def new_product():
    if login.login() != 'admin':
        print('unauthorised access')
        time.sleep(1)
        update_stock()
    else:
        more = 'n'
        while more == 'n':
            code = input('code : ')
            company = input('company : ')
            product = input('product : ')
            quantity = input('new quantity : ')
            sep = ','
            _ = '\''
            q = 'INSERT INTO stock VALUES(' + _ + code + _ + sep + _ + company + _ + sep + _ + product + _ + ')'
            c.execute(q)
            connection.commit()
            c.execute('select * from unique_stock')
            last_unique_code = 0
            for i in c.fetchall():
                if i[0] == code:
                    if i[3] > last_unique_code:
                        last_unique_code = i[3]
            for i in range(int(quantity)):
                q = 'INSERT INTO unique_stock VALUES(' + _ + code + _ + sep + _ + str('0'*(5-len(str(last_unique_code+i+1))))+str(last_unique_code+i+1) + _ + ')'
                print(q)
                c.execute(q)
                connection.commit()
            if input('stop?(y) : ') == 'y':
                more = 'y'



def view_stock():
    if login.login() != 'admin':
        print('unauthorised access')
        time.sleep(1)
        return False
    else:
        c.execute('SELECT * FROM stock')
        print('(code , company, product)')
        for i in c.fetchall():
            print(i)
        input('')

def view_unique_stock():
    if login.login() != 'admin':
        print('unauthorised access')
        time.sleep(1)
        return False
    else:
        c.execute('SELECT * FROM unique_stock')
        print('(code, unique_code)')
        for i in c.fetchall():
            print(i)
        input('')





'''def product_bought(list_containing_uniquecode, phone_no):
    sno = coustomer.return_sno_from_phone_no(phone_no)
    for i in range(int((len(list_containing_uniquecode)-1)//2)):
        c.execute('UPDATE unique_stock SET soldto = {} WHERE code = {} and unique_code = {} '.format(sno, list_containing_uniquecode[i + 1], list_containing_uniquecode[i + 2]))

'''

