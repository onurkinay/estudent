

class Student:
    def __init__(self, id, name, surname, phone, email, number, room):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.number = number
        self.room = room


class Teacher:
    def __init__(self, id, name, surname, phone, email, position):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.position = position


class Lesson:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Room:
    def __init__(self, id, name, lessons, teachers):
        self.id = id
        self.name = name
        self.lessons = lessons
        self.teachers = teachers


