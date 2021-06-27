# sales

import time
import sys
import sqlite3
import login
import stock
import bill




connection = sqlite3.connect('sales.db')
c = connection.cursor()

try:
    c.execute('CREATE TABLE sales(sno INT(5) PRIMARY KEY, time varchar(20), phone_no VARCHAR(15), billno varchar(10), type varchar(5))')
    #c.execute('CREATE TABLE bill(billno INT(5) PRIMARY KEY, uniquecode1 VARCHAR(20), uniquecode2 VARCHAR(20), uniquecode3 VARCHAR(20), uniquecode4 VARCHAR(20), uniquecode5 VARCHAR(20), uniquecode6 VARCHAR(20), uniquecode7 VARCHAR(20), uniquecode8 VARCHAR(20), uniquecode9 VARCHAR(20), uniquecode10 VARCHAR(20), uniquecode11 VARCHAR(20), uniquecode12 VARCHAR(20), uniquecode13 VARCHAR(20), uniquecode14 VARCHAR(20), uniquecode15 VARCHAR(20), uniquecode16 VARCHAR(20), uniquecode17 VARCHAR(20), uniquecode18 VARCHAR(20), uniquecode19 VARCHAR(20), uniquecode20 VARCHAR(20), uniquecode21 VARCHAR(20), uniquecode22 VARCHAR(20), uniquecode23 VARCHAR(20), uniquecode24 VARCHAR(20), uniquecode25 VARCHAR(20))')
    connection.commit()
    # sno, time (automatic), phone_no, billno, type
    # removed!  billno (PK), uniquecode1, uniquecode2, uniquecode3... uniquecode25
except:
    pass


def currdate():
    t = time.ctime(time.time())
    t = t[4:10] + ' ' + t[-4:]
    t = t.split()
    if t[0] == 'Jan':
    	t[0] = "1"
    if t[0] == 'Feb':
    	t[0] = '2'
    if t[0] == 'Mar':
    	t[0] = '3'
    if t[0] == 'Apr':
    	t[0] = '4'
    if t[0] == 'May':
    	t[0] = '5'
    if t[0] == 'Jun':
        t[0] = '6'
    if t[0] == 'Jul':
    	t[0] = '7'
    if t[0] == 'Aug':
    	t[0] = '8'
    if t[0] == 'Sep':
    	t[0] = '9'
    if t[0] == 'Oct':
    	t[0] = '10'
    if t[0] == 'Nov':
    	t[0] = '11'
    if t[0] == 'Dec':
    	t[0] = '12'
    return str(t[0]+t[1]+t[2])


def create_bill(phone_no):
    phone_no = phone_no
    c.execute('SELECT * FROM sales')
    billno = str(len(c.fetchall()) + 1)
    data = []
    data.append(billno)
    more = 'y'
    while more == 'y':
        data.append(input('Enter the common code : '))
        data.append(input('Enter the barcode/unique code : '))
        if input('continue [y/n] ')=='n':
            more = 'n'
    bill.save_bill(data)
    bill.print_bill(data)
    return billno

def on_spot_sales():
    #sno, time (automatic), phone_no, billno, type
    c.execute('SELECT * FROM sales')
    olddata = c.fetchall()
    data = []
    data.append(str(len(olddata) + 1))
    data.append(currdate())
    phone_no = input('Please enter phone no.')
    data.append(phone_no)
    billno = create_bill(phone_no)
    data.append(billno)
    data.append('spot, ' + input('cash or card? : '))
    sep = ','
    _ = '\"'
    q = 'INSERT INTO sales(sno, time, phone_no, billno, type) VALUES(' + data[0] + sep + _ + data[1] + _ + sep + _ + data[2] + _ + sep + _ + data[3] + _ + sep + _ + data[4] + _ + ')'
    print(data, q)
    #has 6 rows but only 5 values were supplied!
    c.execute(q)
'''    try:
        c.execute(q)
    except:
        print('error...try again')
        on_spot_sales()'''



def phone_order():
    print('under construction...')
    time.sleep(1)

def online_order():
    print('under construction...')
    time.sleep(1)

def view_sales():
    login_info = login.login()
    if login_info != 'admin':
        print('unauthorised access')
        time.sleep(1)
    else:
        c.execute('SELECT * FROM sales')
        content = c.fetchall()
        if len(content) == 0:
            print('no content')
            input('')
        else:
            for i in content:
                print(i)
            input('')



