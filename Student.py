class Student:

    schoolName = "ABC School"

    def __init__(self, name, roll):

        self.name = name
        self.roll = roll

    def getter(self):
        print(self.schoolName)
        print(self.name, self.roll)

    @classmethod
    def setter(cls, newName):
        cls.schoolName = newName

    stu1 = Student(name='Alex', roll = 10)
    stu1.getter()