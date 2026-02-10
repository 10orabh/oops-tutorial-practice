class Employee:
    def __init__(self,id,salary,designation):
        self.id = id
        self.salary = salary
        self.designation = designation

    def show(self):
        print(f"id = {self.id}")
        print(f"salary = {self.salary}")
        print(f"designation = {self.designation}")
        
    
emp1 = Employee(24360,20000,"Assitant_professor")
emp1.show()

