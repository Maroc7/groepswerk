import user
import task
import db

user_list = []
C_ACTION_MAKE_TASK = 1
C_ACTION_MAKE_USER = 2
C_ACTION_SHOW_USER = 3
C_ACTION_DELETE_USER = 4
C_STOP = 99
C_ACTIONS = [C_ACTION_MAKE_TASK,C_ACTION_MAKE_TASK,C_ACTION_SHOW_USER, C_ACTION_DELETE_USER]


def menu_header() -> int:
    """
    Summary line.
    Prints out the menu header and asks the user for an choice (int)
    Parameters:
    Returns: choice
    int: Description of return value
  
    """
    print("-"*35)
    print("-"*35)
    print("MENU")
    print("")
    print(f'{C_ACTION_MAKE_TASK}. Create task')
    print(f'{C_ACTION_MAKE_USER}. Create user')
    print(f'{C_ACTION_SHOW_USER}. Show users')
    print(f'{C_ACTION_DELETE_USER}. Delete user')
    print(f'{C_STOP}. Stop program')
    print("-"*35)
    print("-"*35)

    try:
        print("")
        choice = int(input("Make your choice: "))
    except Exception as e:
        print("Select choice by given int,{}".format(e))
        menu_header()
    return choice



def do_menu():
    """
    Summary line.
    runs functions of choice
    return: nothing
    """
    loop = True
    while loop:
        choice = menu_header()
        if choice == C_ACTION_MAKE_TASK:
            task.do_all()
        if choice == C_ACTION_MAKE_USER:
            user.add_user()
        if choice == C_ACTION_SHOW_USER:
            user.show_users()
        if choice == C_ACTION_DELETE_USER:
            user.delete_user()
        if choice == C_STOP:
            loop = False

if __name__ == "__main__":
    db.get_sql_lite_connection()
    do_menu()
    db.close_sql_lite_connection()