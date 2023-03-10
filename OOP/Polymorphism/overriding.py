class Employee:
    def __init__(self):
        self.numberOfWorkingHours = None

    def setNumberOfWorkingHours(self):
     self.setNumberOfWorkingHours = 40
     def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)
class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours  = 45

employee = Employee()
employee.setNumberOfWorkingHours
print("Number of working hours of employee: ", end=' ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end=' ')
print("Number of working hours of trainee:", end = ' ')
trainee.displayNumberOfWorkingHours()
class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45


employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = '  ')
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end= ' ')
