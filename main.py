import user
import task
import db
import inputs
import client



user_list = []
client_list = []


#actions task: 
C_ACTION_MENU_TASK = 11
C_ACTION_MAKE_TASK = 1
C_ACTION_SHOW_TASK = 2
C_ACTION_DELETE_TASK = 3
#actions users:
C_ACTION_MENU_USER = 22
C_ACTION_MAKE_USER = 4
C_ACTION_SHOW_USER = 5
C_ACTION_DELETE_USER = 6

#actions clients:
C_ACTION_MENU_CLIENT = 33
C_ACTION_MAKE_CLIENT = 7
C_ACTION_SHOW_CLIENT = 8
C_ACTION_DELETE_CLIENT = 9




C_ACTION_RETURN = 0
C_STOP = 99
C_ACTIONS = [C_ACTION_MAKE_TASK,C_ACTION_MAKE_TASK,C_ACTION_DELETE_TASK,C_ACTION_SHOW_USER, C_ACTION_DELETE_USER,C_ACTION_RETURN,C_ACTION_MENU_TASK]


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
    #task menu
    print(f"{C_ACTION_MENU_TASK}. Task")
    #user
    print(f"{C_ACTION_MENU_USER}. User")
    print(f"{C_ACTION_MENU_CLIENT}. Client")
    print(f'{C_STOP}. Stop program')
    print("-"*35)
    print("-"*35)

    try:
        print("")
        choice = int(input("Make your choice: "))
    except Exception as e:
        print("Select choice by given int,{}".format(e))
        choice = menu_header()
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
        #special menu for task
        if choice ==C_ACTION_MENU_TASK:
            loop = False
            menu_task()
        #user mrnu
        if choice == C_ACTION_MENU_USER:
            loop = False
            menu_user()
        # client menu
        if choice == C_ACTION_MENU_CLIENT:
            loop = False
            menu_client()
        if choice == C_STOP:
            loop = False


def menu_task_header():
    print("-"*35)
    print("-"*35)
    print("TASK MENU")
    print("")
    print(f'{C_ACTION_MAKE_TASK}. Create task')
    print(f'{C_ACTION_SHOW_TASK}. Show task')
    print(f'{C_ACTION_DELETE_TASK}. Delete task')
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-"*35)
    print("-"*35)


def menu_task():
    """
    this is an sub-menu for tasks.
    """
    menu_task_header()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ",1)
    
        if choice == C_ACTION_MAKE_TASK:
            task.create_tasks()
            menu_task_header()
        if choice == C_ACTION_SHOW_TASK:
            task.show_task()
            menu_task_header()
        if choice == C_ACTION_DELETE_TASK:
            task.delete_task()
            menu_task_header()
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()


def menu_header_user():
    print("-"*35)
    print("-"*35)
    print("USER MENU")
    print("")
    print(f'{C_ACTION_MAKE_USER}. Create user')
    print(f'{C_ACTION_SHOW_USER}. Show users')
    print(f'{C_ACTION_DELETE_USER}. Delete user')
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-"*35)
    print("-"*35)


def menu_user():
    """
    this is an sub-menu for tasks.
    """
    menu_header_user()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ",1)
    
        if choice == C_ACTION_MAKE_USER:
            user.add_user()
            menu_header_user()
        if choice == C_ACTION_SHOW_USER:
            user.User.show_users()
            menu_header_user()
        if choice == C_ACTION_DELETE_USER:
            user.delete_user()
            menu_header_user()
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()

def menu_client_header():
    print("-"*35)
    print("-"*35)
    print("MENU CLIENT")
    print("")
    print(f'{C_ACTION_MAKE_CLIENT}. Create CLIENT')
    print(f'{C_ACTION_SHOW_CLIENT}. Show CLIENT')
    print(f'{C_ACTION_DELETE_CLIENT}. Delete CLIENT')
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-"*35)
    print("-"*35)



def menu_client():
    menu_client_header()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ", 1)

        if choice == C_ACTION_MAKE_CLIENT:
            client.add_client()
            menu_client_header()
        if choice == C_ACTION_SHOW_CLIENT:
            client.show_clients()
            menu_header_user()
        if choice == C_ACTION_DELETE_CLIENT:
            client.delete_client()
            menu_client_header()
        if choice == C_ACTION_RETURN:
            loop = False
            do_menu()

if __name__ == "__main__":
    try:
        db.get_sql_lite_connection()
        do_menu()
    except Exception as e:
        print(f'something went wrong: {e}')
    finally:
        db.close_sql_lite_connection()
