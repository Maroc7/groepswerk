import user
import task
user_list = []
C_ACTION_MAKE_TASK = 1
C_ACTION_MAKE_USER = 2
C_ACTION_SHOW_USER = 3
C_ACTIONS = [C_ACTION_MAKE_TASK,C_ACTION_MAKE_TASK,C_ACTION_SHOW_USER]


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
    print("-"*35)
    print("-"*35)

    try:
        print("")
        choice = int(input("Make youre choice: "))
    except Exception as e:
        print("Select choice by given int,{}".format(e))
        menu_header()
    return choice



def do_menu(choice:int):
    """
    Summary line.
    runs functions of choice
    return: nothing
    """

    if choice == C_ACTION_MAKE_TASK:
        task.do_all()
    if choice == C_ACTION_MAKE_USER:
        user.add_user(user_list)
        user.show_users(user_list)
    if choice == C_ACTION_SHOW_USER:
        user.show_users(user_list)




def do_run():
    choice = menu_header()
    do_menu(choice)

do_run()