class Employee:
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")
employeeOne = Employee()
employeeOne.name

employeeOne.hasAchievedTarget()
employeeTwo = Employee()
print(employeeTwo.name)

numbers = [1, 2, 3]
type(numbers)
numbers.append(4)