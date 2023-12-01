import sqlite3
from contextlib import contextmanager

database = "./university.db"

class OperationResult:
    is_ok = False
    message = ""
    error = None
    result = None

    def set_values(self, is_ok: bool=False, error=None, result=None):
        self.is_ok = is_ok
        if error:
            self.error = error
            self.message = str(error)
        if is_ok:
            self.message = "Command successfully ecxecuted!"
        self.result = result

@contextmanager
def create_connection(database):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(database)
        yield conn
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()

def execute_command(conn, sql_command: str):
    """ create a table from the execute_sql statement
    :param conn: Connection object
    :param sql_command: SQL command as string
    :return:
    """
    result = OperationResult()
    try:
        cur = conn.cursor()
        cur.execute(sql_command)
        result.set_values(is_ok=True)
    except sqlite3.Error as e:
        result.set_values(error=e)

    return result

def execute_query(conn, sql_query: str, params: tuple):
    result = OperationResult()
    try:
        cur = conn.cursor()
        cur.execute(sql_query, params)
        result.set_values(is_ok=True, result=cur.fetchall())
    except sqlite3.Error as e:
        result.set_values(error=e)
    finally:
        cur.close()

    return result

            