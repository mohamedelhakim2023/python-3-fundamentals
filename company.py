from employee import Employee, SalaryEmployee, HourlyEmployee

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        
    def display_employees(self):
        print("Employees:")
        for employee in self.employees:
            print(employee.fname, employee.lname)
        print("-----------------") 
  
        
def main():
    my_company = Company()
    employee1 = SalaryEmployee("John", "Doe", 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("doe", "er", 40, 15)
    my_company.add_employee(employee2)
    
    my_company.display_employees()
    amount = SalaryEmployee.calculate_paycheck(employee1)
    print(amount)
    amount = HourlyEmployee.calculate_paycheck(employee2)
    print(amount)

main()             