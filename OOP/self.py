age = 3
class Employee:
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name= ", self.name)
        age = 30
        print("Age= ", age)
    def printEmployeeDetails(self):
        print("Printing in another world")
        print("Name ", self.name)
        print("Age: ", age)
        
employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()

