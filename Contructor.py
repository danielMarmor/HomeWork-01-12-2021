from Employee import Employee


class Contructor(Employee):
    def __init__(self, id, name, address, year_of_birth, number_of_projects, project_rate):
        super().__init__(id, name, address, year_of_birth)
        self.number_of_projects = number_of_projects
        self.project_rate = project_rate

    def calculate_salary(self):
        salary = self.number_of_projects * self.project_rate
        return salary

    def __str__(self):
        return super().__str__() + f', Number of Projects={self.number_of_projects}, Project Rate={self.project_rate},' \
                                     f'Age={self.get_age()} Salary= {self.calculate_salary()}'

