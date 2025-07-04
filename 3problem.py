class Employee:
    salary = 23456
    increment = 100


    @property
    def salaryAfterIncrement(self):
        return(self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100
    

e = Employee()    
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 46982.0
print(e.increment)  