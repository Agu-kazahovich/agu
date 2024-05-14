class Person:
    def __init__(self,name):
        self.name = name
    def get_info(self):
        print("Аты:",self.name)

class Employee(Person):
    def job(self,job_name):
        print("Аты:",self.name,"жұмысы:",job_name)

employe_obj = Employee("Ағыбай")
employe_obj.job("prog")



class Figura:
    def __init__(self, p):
        self.p = p
    
    def get_info(self):
        print("Периметр:", self.p)

class Triangle(Figura):
    def __init__(self, a, b, c):
        super().__init__(a + b + c)

triangle_obj = Triangle(10, 20, 30)
triangle_obj.get_info()
