#class  A :
   # attr = 'Helo world'
   # def hello(self):
    #    print(self.attr)

#obj1 = A()
#hello = obj1.hello()
#print(hello)



class Person:
    def __init__(self,name,age,surname=""):
        self.name = name
        self.age = age
        self.surname = surname

    def my_method(self):
        if self.surname:
            print("Менің атым "+ self.name, self.surname ,"жасым " ,self.age, "де "   )
        else:
            print("Менің атым "+ self.name,"жасым " ,self.age, "де " )
       
p1 = Person("Agibay",18,"Bisamet")
p1.my_method()
p1 = Person("Agibay",18,"")
p1.my_method()





class Car:
    def __init__(self,marc,subname,age):
        self.marc = marc
        self.subname = subname
        self.age = age

    def my(self):
        print("Марка "+ self.marka, self.subname , self.age)

p1 = Car("Tayota", "Camry" , 2024)
p1.my()



       