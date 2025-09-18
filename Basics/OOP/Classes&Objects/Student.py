class Student:
    def set_details(self , name , marks):
        self.name = name
        self.marks = marks
        
student1 = Student()
student1.set_details("Armaan" , 95)
print(student1.name , student1.marks)
