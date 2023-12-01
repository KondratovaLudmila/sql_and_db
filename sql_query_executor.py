from connect_sqlite import *
from re import findall


def get_params(sql: str) -> dict:
    matching =  findall(r"(?<=:)\w+", sql)
    return matching

def main():
    #Read file
    file_name = input("Enter sql-file path: ")
    try:
        with open(file_name, "r") as f:
            sql_script = f.read()
    except Exception as e:
        print(str(e))
        return
    
    #Input parameters
    params = {}
    for name in get_params(sql_script):
        value = input(f"enter {name}: ")
        params[name] = value

    #Open connection
    with create_connection(database) as conn:
        #Execute query
        result = execute_query(conn, sql_script, params)
    
    #Output query result
    print(result.message)
    if result.is_ok:
        for row in result.result:
            print(row)

if __name__ == "__main__":
    main()
