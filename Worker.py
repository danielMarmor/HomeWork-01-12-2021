from Employee import Employee


class Worker(Employee):
    def __init__(self, id, name, address, year_of_birth, hours_per_day, hour_wage):
        super().__init__(id, name, address, year_of_birth)
        self.hours_per_day = hours_per_day
        self.hour_wage = hour_wage

    def calculate_salary(self):
        salary = self.hour_wage * self.hours_per_day
        return salary

    def __str__(self):
        return super().__str__() + f', Hours Per Day={self.hours_per_day}, Hour Wage={self.hour_wage},' \
                                     f'Age={self.get_age()} Salary={self.calculate_salary()}'

