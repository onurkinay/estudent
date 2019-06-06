from tkinter import *
from tkinter import messagebox
from dbfuncs import get_lessons, update_lesson, add_lesson
from models import Lesson


class LessonWindow:

    def __init__(self, rootmain, dbmain):
        self.lessons = None
        self.lesson_name = StringVar()
        self.new_lesson = IntVar()
        self.lesson_id = -1
        self.root = rootmain
        self.db = dbmain

    def lesson_window(self): # new window definition
        lesson_w = Toplevel(self.root)
        self.lessons = get_lessons(self.db)
        lblesson = Listbox(lesson_w)
        lblesson.bind('<<ListboxSelect>>', self.onselect)

        for row in self.lessons:
            lblesson.insert(row[0], row[1])

        lblesson.grid(row=0, sticky=(N, S, E, W))

        form = Frame(lesson_w)
        form.grid(row=1)

        Entry(form, textvariable=self.lesson_name).grid(row=0, column=1)

        Label(form, text="lesson Name: ").grid(row=0, column=0, sticky=W)

        Button(form, text="Submit...", command=self.submit_form).grid(row=6, column=1, sticky=E)
        Checkbutton(form, text="new lesson?", variable=self.new_lesson).grid(row=6, column=0)

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])

        self.lesson_name.set(self.lessons[index][1])
        self.lesson_id = self.lessons[index][0]
        self.new_lesson.set(0)

    def submit_form(self):
        lesson = Lesson(self.lesson_id, self.lesson_name.get())

        if self.new_lesson.get() == 1:
            add_lesson(self.db, lesson)
        else:
            update_lesson(self.db, lesson, self.lesson_id)

        messagebox.showinfo("Okey!", "Your order has been applied")