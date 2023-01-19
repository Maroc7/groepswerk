import user
import task
import db
import inputs
import project
user_list = []

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
#actions projects:
C_ACTION_MENU_PROJECT = 33
C_ACTION_MAKE_PROJECT = 7
C_ACTION_SHOW_PROJECT = 8

C_ACTION_RETURN = 0

C_STOP = 99
C_ACTIONS = [C_ACTION_MAKE_TASK,C_ACTION_MAKE_TASK,C_ACTION_DELETE_TASK,C_ACTION_SHOW_USER, C_ACTION_DELETE_USER,C_ACTION_RETURN,C_ACTION_MENU_TASK,C_ACTION_MENU_PROJECT,C_ACTION_MAKE_PROJECT,C_ACTION_SHOW_PROJECT]


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
    #project
    print(f"{C_ACTION_MENU_PROJECT}. Project")
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
        #user menu
        if choice == C_ACTION_MENU_USER:
            loop = False
            menu_user()
        #project menu
        if choice == C_ACTION_MENU_PROJECT:
            loop = False
            menu_project()            
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


def menu_project_header():
    print("-"*35)
    print("-"*35)
    print("PROJECT MENU")
    print("")
    print(f'{C_ACTION_MAKE_PROJECT}. Create project')
    print(f'{C_ACTION_SHOW_PROJECT}. Show projects')
    print(f'{C_ACTION_RETURN}. Return to main menu')
    print("-"*35)
    print("-"*35)


def menu_project():
    """
    this is an sub-menu for projects.
    """
    menu_project_header()
    loop = True
    while loop:
        choice = inputs.get_input_item("Choice: ",1)
    
        if choice == C_ACTION_MAKE_PROJECT:
            project.create_project()
            menu_project_header()
        if choice == C_ACTION_SHOW_PROJECT:
            project.show_projects()
            menu_project_header()
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