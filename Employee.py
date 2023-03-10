class Employee:
    def __init__(self, name):
        self.name = "Mark"
    def enterEmployeeDetails(self):
        self.name = "Mark"

    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Mark")
employeeTwo = Employee("Matthew")
employee.displayEmployeeDetails()
employee.displayEmployeeDetails()