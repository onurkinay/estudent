from tkinter import *
from tkinter import messagebox
from dbfuncs import get_rooms, update_room, add_room, get_teachers, get_lessons
from models import Room


class RoomWindow:

    def __init__(self, rootmain, dbmain):
        self.rooms = None
        self.room_name = StringVar()
        self.room_lessons = StringVar()
        self.room_teachers = StringVar()
        self.new_room = IntVar()
        self.room_id = -1
        self.root = rootmain
        self.db = dbmain

        self.teachers = get_teachers(self.db)
        self.lessons = get_lessons(self.db)

    def room_window(self): # new window definition
        room_w = Toplevel(self.root)
        self.rooms = get_rooms(self.db)
        lbroom = Listbox(room_w)
        lbroom.bind('<<ListboxSelect>>', self.onselect)

        for row in self.rooms:
            lbroom.insert(row[0], row[1])

        lbroom.grid(row=0, sticky=(N, S, E, W))

        form = Frame(room_w)
        form.grid(row=1)

        Entry(form, textvariable=self.room_name).grid(row=0, column=1)

        self.lblessons = Listbox(form, selectmode="multiple", exportselection=0)
        for lesson in self.lessons:
            self.lblessons.insert(END, lesson[1])
        self.lblessons.grid(row=1, column=1)

        self.lbteachers = Listbox(form, selectmode="multiple", exportselection=0)
        for teacher in self.teachers:
            self.lbteachers.insert(END, teacher[1])
        self.lbteachers.grid(row=2, column=1)

        Label(form, text="Room Name: ").grid(row=0, column=0, sticky=W)
        Label(form, text="Room Lessons: ").grid(row=1, column=0, sticky=W)
        Label(form, text="Room Teachers: ").grid(row=2, column=0, sticky=W)

        Button(form, text="Submit...", command=self.submit_form).grid(row=6, column=1, sticky=E)
        Checkbutton(form, text="new Room?", variable=self.new_room).grid(row=6, column=0)

    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])

        self.lbteachers.select_clear(0, 'end')
        self.lblessons.select_clear(0, 'end')

        self.room_name.set(self.rooms[index][1])
        self.room_lessons.set(self.rooms[index][2])
        self.room_id = self.rooms[index][0]
        self.new_room.set(0)

        for item in self.rooms[index][2].split(','):
            i = 0
            for lesson in self.lessons:
                if item == str(lesson[0]):
                    self.lblessons.select_set(i)
                    break
                i += 1

        for item in self.rooms[index][3].split(','):
            i = 0
            for teacher in self.teachers:
                if item == str(teacher[0]):
                    self.lbteachers.select_set(i)
                    break
                i += 1

    def get_lessons_from_lb(self):
        # Note here that Tkinter passes an event object to onselect()
        lessons_result = []
        for item in self.lblessons.curselection():
            lessons_result.append(str(self.lessons[item][0]))
        self.room_lessons.set(','.join(lessons_result))

    def get_teachers_from_lb(self):
        teachers_result = []
        for item in self.lbteachers.curselection():
            teachers_result.append(str(self.teachers[item][0]))
        self.room_teachers.set(','.join(teachers_result))

    def submit_form(self):
        self.get_lessons_from_lb()
        self.get_teachers_from_lb()

        room = Room(self.room_id, self.room_name.get(), self.room_lessons.get(), self.room_teachers.get())

        if self.new_room.get() == 1:
            add_room(self.db, room)
        else:
            update_room(self.db, room, self.room_id)

        messagebox.showinfo("Okey!", "Your order has been applied")

