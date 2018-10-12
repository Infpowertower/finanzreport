# this is a pure console application for debugging and testing
import logging
import database_helper as db


def create_menu(quit, *entry):
    i = 0
    for x in entry:
        print(str(i)+"\t"+x)
        i += 1
    if quit:
        print("9\tquit")
    choice = input("What's it gonna be?\n")
    return choice


def start():
    print("Welcome to Finanzreport (name subject to change)")
    quit = False
    while 1:
        choice = create_menu(False, 'quit', 'usermode', 'debugmode')
        if choice == '1':
            quit = usermode()
        elif choice == '2':
            quit = debugmode()
        elif choice == '0':
            break
        else:
            print("Invalid input! Try again.")
        if quit:
            break


def debugmode():
    # this mode is to test all functions, e.g. to manage the databases without restrictions
    print("Welcome to the underworld!")
    while 1:
        choice = create_menu(True, 'back', 'databases', 'logging')
        if choice == '1':
            debug_data()
        if choice == '2':
            debug_data()
        if choice == '0':
            break
        elif choice == '9':
            return True;
    return False


def debug_data():
    while 1:
        choice = create_menu(True, 'back', 'show', 'delete', 'create', 'insert', 'select')
        if choice == 0:
            break
        elif choice == 9:
            return True


def debug_logging():
    pass


class UserData:
    def __init__(self, username):
        self.username = username
        data = db.execute_sql('db_test', 'SELECT * FROM user WHERE username="{}"'.format(username))[0]
        self.id = data[0]
        self.name = data[2]
        self.surname = data[3]


def usermode():
    # this mode simulates the user experience without a fancy web UI (which is coming later)
    print("This is the usermode")
    while 1:
        user = UserData('infpowertower')
        print("Welcome {} {}".format(user.name, user.surname))
        break
    return False
