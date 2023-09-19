class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    def calculate_paycheck(self):
        return self.salary / 52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate
        
    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_number, commission_rate):
        super().__init__(fname, lname, salary)
        self.sales_number = sales_number
        self.commission_rate = commission_rate
        
    def calculate_paycheck(self):
        regular_pay = super().calculate_paycheck()
        commission_pay = self.sales_number * self.commission_rate
        return regular_pay + commission_pay

       
   
    
        