class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=name
        print(self.name,self.age)
        self.Computer()
    class Computer:
        def __init__(self):
            self.brand="Dell"
            self.cpu="i5"
        def dispaly(self):
            print(self.brand,self.cpu)
Student("Mg Mg",18)
Student.Computer().dispaly()