import user
import task
user_list = []

def do_run():
    """main loop
    """
    user.add_user(user_list)
    user.show_users(user_list)
    task.do_all()


if __name__ == '__main__':
    do_run()
