from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def __init__(self, name, age, genre, job):
        self.name = name
        self.age = age
        self.genre = genre
        self.job = job

    @abstractclassmethod
    def work():
        pass

    def introduction(self):
        print(f"Hello ")
