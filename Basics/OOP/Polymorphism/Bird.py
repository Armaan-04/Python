 #polymorphism with classes method overridng
class Bird():
     def sound(self):
         print("Birds make sound")
         
class Crow(Bird):
    def sound(self):
        print("Crows say 'Caw Caw' ")

class parrot(Bird):
    def sound(self):
        print("Parrots sounds 'squak' ")
        
bird1 = Crow()
bird2 = parrot()

bird1.sound()
bird2.sound()