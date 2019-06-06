from tkinter import *
from tkinter import ttk, messagebox
from dbfuncs import get_students, update_student, add_student, get_rooms
from models import Student


class StudentWindow:

    def __init__(self, rootmain, dbmain):
        self.students = None
        self.student_name = StringVar()
        self.student_surname = StringVar()
        self.student_phone = StringVar()
        self.student_email = StringVar()
        self.student_number = StringVar()
        self.student_room = StringVar()
        self.student_room_id = -1
        self.new_student = IntVar()
        self.student_id = -1
        self.root = rootmain
        self.db = dbmain
        self.main_rooms = self.get_room_names()

    def student_window(self): # new window definition
        student_w = Toplevel(self.root)
        self.students = get_students(self.db)
        lbstudent = Listbox(student_w)
        lbstudent.bind('<<ListboxSelect>>', self.onselect)

        for row in self.students:
            lbstudent.insert(row[0], row[1])

        lbstudent.grid(row=0, sticky=(N, S, E, W))

        form = Frame(student_w)
        form.grid(row=1)

        Entry(form, textvariable=self.student_name).grid(row=0, column=1)
        Entry(form, textvariable=self.student_surname).grid(row=1, column=1)
        Entry(form, textvariable=self.student_phone).grid(row=2, column=1)
        Entry(form, textvariable=self.student_email).grid(row=3, column=1)
        Entry(form, textvariable=self.student_number).grid(row=4, column=1)

        rooms_names = []
        self.main_rooms = self.get_room_names()
        for row in self.main_rooms:
            rooms_names.append(row[1])

        ttk.Combobox(form, values=rooms_names,
                     textvariable=self.student_room).grid(row=5, column=1)

        Label(form, text="Student Name: ").grid(row=0, column=0, sticky=W)
        Label(form, text="Student Surname: ").grid(row=1, column=0, sticky=W)
        Label(form, text="Student Phone: ").grid(row=2, column=0, sticky=W)
        Label(form, text="Student E-Mail: ").grid(row=3, column=0, sticky=W)
        Label(form, text="Student Number: ").grid(row=4, column=0, sticky=W)
        Label(form, text="Student Room: ").grid(row=5, column=0, sticky=W)

        Button(form, text="Submit...", command=self.submit_form).grid(row=6, column=1, sticky=E)
        Checkbutton(form, text="new student?", variable=self.new_student).grid(row=6, column=0)

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])

        self.student_name.set(self.students[index][1])
        self.student_surname.set(self.students[index][2])
        self.student_phone.set(self.students[index][3])
        self.student_email.set(self.students[index][4])
        self.student_number.set(self.students[index][5])
        self.student_room.set(self.main_rooms[self.students[index][6]-1][1])
        self.student_room_id = int(self.main_rooms[self.students[index][6]-1][0])
        self.student_id = self.students[index][0]
        self.new_student.set(0)

    def get_room_names(self):
        rooms = get_rooms(self.db)
        lesson_names = []
        for row in rooms:
            lesson_names.append([row[0], row[1]])
        return lesson_names

    def submit_form(self):

        for room in self.main_rooms:
            if room[1] == self.student_room.get():
                self.student_room_id = room[0]
                break

        student = Student(self.student_id, self.student_name.get(), self.student_surname.get(),
                        self.student_phone.get(),
                        self.student_email.get(), self.student_number.get(),
                        self.student_room_id)

        if self.new_student.get() == 1:
            add_student(self.db, student)
        else:
            update_student(self.db, student, self.student_id)

        messagebox.showinfo("Okey!", "Your order has been applied")
