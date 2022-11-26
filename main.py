import user
user_list = []

def do_run():
    """main loop
    """
    user.add_user(user_list)
    user.show_users(user_list)


if __name__ == '__main__':
    do_run()