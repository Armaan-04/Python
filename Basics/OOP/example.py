class Character:
    def __init__ (self , name , health , attack):  #__init__ to define a constructor in python
        self.name = name
        self.health = health
        self.attack = attack
        
    def attack_enemy(self):
        print(f"{self.name} attacks with power {self.attack} with health {self.health}")
    
warrior = Character("Thor" , 100 , 50)
mage = Character("Gandalf" , 80 , 70)
archer = Character("Archer" , 80 , 90)

warrior.attack_enemy()
mage.attack_enemy()  
archer.attack_enemy()  