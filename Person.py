class Person():
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality 
    def talk(self):
        print("Hello, I'm talking a little")

class Artist():
    def __init__(self, hability):
        self.hability = hability
    def show_hability(self):
        print(f"My hability is: {self.hability}")


class ArtistEmployee(Person, Artist):
    def __init__(self, name, age, nacionality, hability, salary, job):
        Person.__init__(self, name, age, nacionality)
        Artist.__init__(self, hability)
        self.salary = salary
        self.job = job
    def presentation(self):
        return f'My hability is {super.show_hability()}'        



class Employee(Person):
    def __init__(self, name, age, nacionality, salary, job):
        super().__init__(name, age, nacionality)
        self.salary = salary
        self.job = job

class Student(Person):
    def __init__(self, name, age, nacionality, grades, university):
        super().__init__(name, age, nacionality)
        self.grades = grades
        self.university = university
