#shop

#importing python modules
import time
import os
import sys
import sqlite3
import pyautogui
import subprocess

#importing coustome made modules
import login
import stock
import coustomer
import sales
import contact_admin



def start():
    login_info = login.login()
    if login_info == 'admin':
        admin_menu()
    elif login_info == '0':
        menu()
    else:
        print('unauthorised access')
        print('please try again')
        time.sleep(1)
        


def admin_menu():
    print('\n\n1. view sales \n2. update stock \n3. new_product \n4. view stock \n5. view unique stock \n6. view coustomer data \n7. view all accounts \n8. logout\n9. Exit')
    choice = input('Enter : ')
    if choice == '1':
        sales.view_sales()
    elif choice == '2':
        stock.update_stock()
    elif choice == '3':
        stock.new_product()
    elif choice == '4':
        stock.view_stock()
    elif choice == '5':
        stock.view_unique_stock()
    elif choice == '6':
        coustomer.see_all_data()
    elif choice == '7':
        login.view_all_data(username = input('username : '), password = input('password : '))
    elif choice == '8':
        logout()
    elif choice == '9':
        exit_function()
    else:
        admin_menu()

    

def menu():
    print('\n\n1. sales \n2. phone order \n3. online order \n4. new coustomer \n5. contact admin \n6. logout \n7. Exit')
    choice = input('Enter : ')
    if choice == '1':
        sales.on_spot_sales()
    elif choice == '2':
        sales.phone_order()
    elif choice == '3':
        sales.online_order()
    elif choice == '4':
        coustomer.new()
    elif choice == '5':
        #contact_admin.contact_admin()
        print('under development...')
        time.sleep(1)
    elif choice == '6':
        logout()
    elif choice == '7':
        exit_function()
    else:
        menu()

def logout():
    f = open('user.txt', 'w')
    f.write('')
    start()


def exit_function():
    exit()




os.system('color A')
while True:
    start()

