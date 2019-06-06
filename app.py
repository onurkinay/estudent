import sqlite3
from tkinter import *
from dbfuncs import *
from models import *


from teach import *
from les import LessonWindow
from rooms import RoomWindow
from stud import StudentWindow

root = Tk()

db = sqlite3.connect('data.db')
create_db(db)


def open_student_window():
    StudentWindow(root, db).student_window()


def open_teacher_window():
     TeacherWindow(root, db).teacher_window()


def open_rooms_window():
     RoomWindow(root, db).room_window()


def open_lessons_window():
    LessonWindow(root, db).lesson_window()


Button(text="Students", width=10, command=open_student_window).place(x=10, y=5)
Button(text="Teachers", width=10,  command=open_teacher_window).place(x=120, y=5)
Button(text="Lessons", width=10, command=open_lessons_window).place(x=230, y=5)
Button(text="Rooms", width=10, command=open_rooms_window).place(x=340, y=5)

Label(text="There are "+str(len(get_students(db)))+" students, "
                       +str(len(get_teachers(db)))+" teachers, "
                       +str(len(get_lessons(db)))+" lessons and "
                       +str(len(get_rooms(db)))+" rooms in the school").place(x=10, y=35)


root.geometry("450x60")
root.mainloop()
