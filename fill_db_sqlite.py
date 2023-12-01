from faker import Faker
from random import randint, choices, shuffle
from connect_sqlite import *
from datetime import timedelta

fake = Faker()
grups = ["SP-3", "OT-2", "KM-5"]
subjects = ["Computer Science", "Mathematical Analysis", "Design and Technology", "Physics", "Machine Learning", "Data Management", "Philosofy"]

MAX_GRUPS = len(grups)
MAX_SUBJECTS = len(subjects)
MAX_STUDENTS = 40
MAX_TEACHERS = 4
MAX_MARKS = 20
MARK_VALUE = 100
DATE_DELTA = "-60d"

sql_insert_grups = """
    INSERT INTO grups(grup)
    VALUES (?);
    """
sql_insert_students = '''
    INSERT INTO students(student, grup_id)
    VALUES (?, ?);
    '''
sql_insert_teachers = '''
    INSERT INTO teachers(teacher)
    VALUES (?);
    '''
sql_insert_subjects = '''
    INSERT INTO subjects(subject, teacher_id)
    VALUES (?, ?);
    '''
sql_insert_marks = '''
    INSERT INTO marks(student_id, mark, date, subject_id)
    VALUES (?, ?, ?, ?);
    '''
def get_grups():
    return [(grup,) for grup in grups]

def get_students():
    return [(fake.name(), randint(1,MAX_GRUPS)) 
            for _ in range(1, MAX_STUDENTS + 1)]

def get_teachers():
    return [(fake.name(),) for _ in range(1, MAX_TEACHERS + 1)]

def get_subjects():
    teachers_id = [id for id in range(1, MAX_TEACHERS + 1)]
    shuffle(teachers_id)
    if MAX_SUBJECTS > MAX_TEACHERS:
        teachers_id.extend(choices(teachers_id, k=MAX_SUBJECTS-MAX_TEACHERS))
    return list(zip(subjects, teachers_id))

def get_marks():
    data = []
    for student_id in range(1, MAX_STUDENTS + 1):
        for _ in range(1, MAX_MARKS + 1):
            subject_id = randint(1, MAX_SUBJECTS)
            mark_date = fake.date_between(DATE_DELTA)
            if mark_date.weekday():
                mark_date = mark_date + timedelta(days=1)
            mark = randint(1, MARK_VALUE)
            data.append((student_id, mark, mark_date, subject_id))
    return data


def fill_tables():
    with create_connection(database) as conn:
        result = OperationResult()
        if not conn:
            result.message = f"Can't conect to db {database}"
            return result
        cur = conn.cursor()
        try:
            #Insert to grups
            cur.executemany(sql_insert_grups, get_grups())
            #Insert into students
            cur.executemany(sql_insert_students, get_students())
            #Insert into teachers
            cur.executemany(sql_insert_teachers, get_teachers())
            #Insert into subjects
            cur.executemany(sql_insert_subjects, get_subjects())
            #Insert into marks
            cur.executemany(sql_insert_marks, get_marks())
            result.set_values(is_ok=True)
        except sqlite3.Error as e:
            result.set_values(error=e)
        finally:
            cur.close()
        
        return result

if __name__ == "__main__":
    result = fill_tables()
    print(result.message)

