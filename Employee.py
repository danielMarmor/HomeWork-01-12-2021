from abc import ABC, abstractmethod
import datetime


class Employee:
    @abstractmethod
    def __init__(self, id, name, address, year_of_birth):
        self.id = id
        self.name = name
        self.address = address
        self.year_of_birth = year_of_birth

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_age(self):
        current_date = datetime.date.today()
        current_year = current_date.year
        age = current_year - self.year_of_birth
        return age

    def __str__(self):
        return f'Id={self.id}, Name={self.name}, Address={self.address}, Year of Birth={self.year_of_birth}'
