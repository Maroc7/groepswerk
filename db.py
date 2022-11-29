import sqlite3


C_DBFILE = 'project.db'
connection, cursor = None, None

        
def get_sql_lite_connection():
    """connect to the database
    """
    global connection
    global cursor
    try:
        connection = sqlite3.connect(C_DBFILE) # Connect to DB and create a cursor
        cursor = connection.cursor()
        print('Database connected')
        return True
    except Exception as e:
        print((f'connection error: {e}'))
        connection = None
        cursor = None
    return False
    

def close_sql_lite_connection():
    """close the connection
    """
    try:
        if connection:
            connection.close()
            print(f'Database connection closed')

    except Exception as e:
        print(f'error: {e}')