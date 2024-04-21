from Human import Human
class Employee(Human):
    def __init__(self,id,name,age,salary,position):
        super(Employee,self).__init__(id,name,age)
        self.salary=salary
        self.position=position

    def see(self):
        print("I can see you")
