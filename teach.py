from tkinter import *
from tkinter import ttk, messagebox

from dbfuncs import get_teachers, update_teacher, add_teacher
from models import Teacher


class TeacherWindow:

    def __init__(self, rootmain, dbmain):
        self.teachers = None
        self.teacher_name = StringVar()
        self.teacher_surname = StringVar()
        self.teacher_phone = StringVar()
        self.teacher_email = StringVar()
        self.teacher_position = StringVar()

        self.new_teacher = IntVar()
        self.teacher_id = -1

        self.root = rootmain
        self.db = dbmain

    def teacher_window(self): # new window definition
        teacher_w = Toplevel(self.root)
        self.teachers = get_teachers(self.db)
        self.lbteacher = Listbox(teacher_w)
        self.lbteacher.bind('<<ListboxSelect>>', self.onselect)

        for row in self.teachers:
            self.lbteacher.insert(row[0], row[1])

        self.lbteacher.grid(row=0, sticky=(N, S, E, W))

        form = Frame(teacher_w)
        form.grid(row=1)

        Entry(form, textvariable=self.teacher_name).grid(row=0, column=1)
        Entry(form, textvariable=self.teacher_surname).grid(row=1, column=1)
        Entry(form, textvariable=self.teacher_phone).grid(row=2, column=1)
        Entry(form, textvariable=self.teacher_email).grid(row=3, column=1)
        ttk.Combobox(form, values=["Instructor", "Professor", "Associate Professor", "Programmer"],
                     textvariable=self.teacher_position).grid(row=4, column=1)

        Label(form, text="Teacher Name: ").grid(row=0, column=0, sticky=W)
        Label(form, text="Teacher Surname: ").grid(row=1, column=0, sticky=W)
        Label(form, text="Teacher Phone: ").grid(row=2, column=0, sticky=W)
        Label(form, text="Teacher E-Mail: ").grid(row=3, column=0, sticky=W)
        Label(form, text="Teacher Position: ").grid(row=4, column=0, sticky=W)

        Button(form, text="Submit...", command=self.submit_form).grid(row=6, column=1, sticky=E)
        Checkbutton(form, text="new teacher?", variable=self.new_teacher).grid(row=6, column=0)

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])

        self.teacher_name.set(self.teachers[index][1])
        self.teacher_surname.set(self.teachers[index][2])
        self.teacher_phone.set(self.teachers[index][3])
        self.teacher_email.set(self.teachers[index][4])
        self.teacher_position.set(self.teachers[index][5])
        self.teacher_id = self.teachers[index][0]
        self.new_teacher.set(0)

    def submit_form(self):

        for teacher in enumerate(self.lbteacher.get(0, END)):
            if teacher[1] == self.teacher_name.get() and self.new_teacher.get() == 0:
                messagebox.showerror("Opps!", "You have forgotten something")
                return

        teacher = Teacher(self.teacher_id, self.teacher_name.get(), self.teacher_surname.get(), self.teacher_phone.get(),
                           self.teacher_email.get(), self.teacher_position.get())

        if self.new_teacher.get() == 1:
            add_teacher(self.db, teacher)
        else:
            update_teacher(self.db, teacher, self.teacher_id)

        messagebox.showinfo("Okey!", "Your order has been applied")