from login import LogIn
from sign_up import SignUp
from homepage import HomePage
from income import Income
from expense import Expense
from transaction import Transaction
from analysis import Analysis
from delete import Delete
from saving import Savings
import database


is_true = True

connection = database.connect()

database.create_create_main_table(connection)
# database.delete(connection)

login_window = LogIn()

while is_true:

    while login_window.sign_up:
        sign_up_window = SignUp()
        if not sign_up_window.is_closed:
            username = sign_up_window.username
            password = sign_up_window.password
            connection = database.connect()
            database.add_user(connection, username, password)
        login_window = LogIn()
        if login_window.is_closed:
            is_true = False

    if login_window.create_homepage:
        homepage_window = HomePage(login_window.table_name)
        while not homepage_window.is_closed:
            if homepage_window.expense:
                expense_window = Expense(login_window.table_name)
                homepage_window = HomePage(login_window.table_name)
            if homepage_window.income:
                income_window = Income(login_window.table_name)
                homepage_window = HomePage(login_window.table_name)
            if homepage_window.transaction:
                transaction_window = Transaction(login_window.table_name)
                homepage_window = HomePage(login_window.table_name)
            if homepage_window.delete:
                delete_window = Delete(login_window.table_name)
                homepage_window = HomePage(login_window.table_name)
            if homepage_window.analysis:
                analysis_window = Analysis(login_window.table_name)
                homepage_window = HomePage(login_window.table_name)
            if homepage_window.suggestion:
                suggestion_window = Savings(login_window.table_name)
                homepage_window = HomePage(login_window.table_name)
        login_window = LogIn()
        if login_window.is_closed:
            is_true = False
    else:
        is_true = False
