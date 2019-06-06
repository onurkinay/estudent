from models import *


def create_db(db):
    cursor = db.cursor()
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, 
                   name TEXT, surname TEXT, phone TEXT, email TEXT unique, 
                                    number INTEGER unique, room INTEGER);
    ''')

    cursor.execute('''  
            CREATE TABLE IF NOT EXISTS teacher(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, phone TEXT, 
                                               email TEXT unique, position TEXT);
    ''')

    cursor.execute('''  
            CREATE TABLE IF NOT EXISTS room(id INTEGER PRIMARY KEY, name TEXT unique, lessons TEXT, teachers TEXT);
    ''')

    cursor.execute('''  
            CREATE TABLE IF NOT EXISTS lessons(id INTEGER PRIMARY KEY, name TEXT unique );
    ''')

    db.commit()

# ADD FUNCTIONS


def add_student(db, student):
    cursor = db.cursor()
    cursor.execute('''INSERT OR IGNORE INTO student(name, surname, phone, email, number, room)
                      VALUES(?,?,?,?,?,?) ''',
                   (student.name, student.surname, student.phone, student.email, student.number, student.room))
    db.commit()
    print(student.name + " was added")


def add_teacher(db, teacher):
    cursor = db.cursor()
    cursor.execute('''INSERT OR IGNORE INTO teacher(name, surname, phone, email, position)
                          VALUES(?,?,?,?,?)''',
                   (teacher.name, teacher.surname, teacher.phone, teacher.email, teacher.position))
    db.commit()


def add_lesson(db, lesson):
    cursor = db.cursor()
    cursor.execute('''INSERT OR IGNORE INTO lessons(name)  VALUES(?)''', (lesson.name,))
    db.commit()


def add_room(db, room):
    cursor = db.cursor()
    cursor.execute('''INSERT OR IGNORE INTO room(name, lessons, teachers)  VALUES(?,?,?)''',
                   (room.name, room.lessons, room.teachers))
    db.commit()

# !ADD FUNCTIONS

# EDIT FUNCTIONS


def update_student(db, student, s_id):
    cursor = db.cursor()
    cursor.execute(''' UPDATE student SET  name=?, surname=?, phone=?, email=?, number=?, room=? WHERE id=?''',
                   (student.name, student.surname, student.phone, student.email, student.number, student.room, s_id))
    db.commit()


def update_teacher(db, teacher, s_id):
    cursor = db.cursor()
    cursor.execute(''' UPDATE teacher SET  name=?, surname=?, phone=?, email=?, position=? WHERE id=?''',
                   (teacher.name, teacher.surname, teacher.phone, teacher.email, teacher.position, s_id))
    db.commit()


def update_lesson(db, lesson, s_id):
    cursor = db.cursor()
    cursor.execute(''' UPDATE lessons SET  name=? WHERE id=?''',
                   (lesson.name, s_id))
    db.commit()


def update_room(db, room, s_id):
    cursor = db.cursor()
    cursor.execute(''' UPDATE room SET  name=?, lessons=?, teachers=? WHERE id=?''',
                   (room.name, room.lessons, room.teachers, s_id))
    db.commit()


# !EDIT FUNCTIONS

# DELETE FUNCTIONS


def del_student(db, s_id):
    cursor = db.cursor()
    cursor.execute(''' DELETE FROM student WHERE id=?''',
                   (s_id,))
    db.commit()


def del_teacher(db, s_id):
    cursor = db.cursor()
    cursor.execute(''' DELETE FROM teacher WHERE id=?''',
                   (s_id,))
    db.commit()


def del_lesson(db, s_id):
    cursor = db.cursor()
    cursor.execute(''' DELETE FROM lessons WHERE id=?''',
                   (s_id,))
    db.commit()


def del_room(db, s_id):
    cursor = db.cursor()
    cursor.execute(''' DELETE FROM room WHERE id=?''',
                   (s_id,))
    db.commit()


# !DELETE FUNCTIONS

def get_students(db):
    cursor = db.cursor()
    cursor.execute(''' SELECT * FROM student ''')

    return cursor.fetchall()


def get_teachers(db):
    cursor = db.cursor()
    cursor.execute(''' SELECT * FROM teacher ''')

    return cursor.fetchall()


def get_lessons(db):
    cursor = db.cursor()
    cursor.execute(''' SELECT * FROM lessons ''')

    return cursor.fetchall()


def get_rooms(db):
    cursor = db.cursor()
    cursor.execute(''' SELECT * FROM room ''')

    return cursor.fetchall()