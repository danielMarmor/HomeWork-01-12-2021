from Employee import Employee


class Manager(Employee):
    def __init__(self, id, name, address, year_of_birth, number_of_emp, emp_rate):
        super().__init__(id, name, address, year_of_birth)
        self.number_of_emp = number_of_emp
        self.emp_rate = emp_rate

    def calculate_salary(self):
        salary = self.number_of_emp * self.emp_rate
        return salary

    def __str__(self):
        return super().__str__() + f', Number of Employees={self.number_of_emp}, Emp Rate={self.emp_rate}, ' \
                                     f'Age={self.get_age()} Salary={self.calculate_salary()}'
