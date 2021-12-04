from Worker import Worker
from Manager import Manager
from Contructor import Contructor

emp1 = Worker(1, 'Daniel Marmor', 'Haifa', 1978, 90, 75)
emp2 = Worker(2, 'Stav Marmor', 'Binyamina', 1985, 108, 80)
emp3 = Manager(3, 'Sara Marmor', 'Tel-Aviv', 1952, 2, 104)
emp4 = Manager(4, 'Baruch Marmor', 'Tel-Aviv', 1950, 7, 809)
emp5 = Contructor(5, 'Anat Doron', 'Jerusalem', 1960, 5, 9500)

print(str(emp1))
print(str(emp2))
print(str(emp3))
print(str(emp4))
print(str(emp5))

