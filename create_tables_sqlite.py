from connect_sqlite import *

#-- Table: groups
sql_create_groups = '''
CREATE TABLE IF NOT EXISTS grups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grup VARCHAR(120) UNIQUE NOT NULL
    );
'''
#-- Table: students
sql_create_students = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR(120) NOT NULL,
    grup_id INTEGER,
    FOREIGN KEY (grup_id) REFERENCES grups (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
'''
#-- Table: teachers
sql_create_teachers = '''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher VARCHAR(120) NOT NULL
    );
'''
#-- Table: subjects
sql_create_subjects = '''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject VARCHAR(120) UNIQUE NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
'''
#-- Table: marks
sql_create_marks = '''
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mark TINYINT UNSIGNED NOT NULL,
    date DATE NOT NULL,
    student_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
'''
sql_commands = (
    sql_create_groups,
    sql_create_students,
    sql_create_teachers,
    sql_create_subjects,
    sql_create_marks,
)

def main():
    with create_connection(database) as conn:
        if conn is None:
            print("Error! cannot create the database connection.")
            return
        for command in sql_commands:
            result = execute_command(conn, command)
            if not  result.is_ok:
                print(command, result.message, sep="\n")
                break
        
if __name__ == "__main__":
    main()
        
