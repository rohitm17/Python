class Enemy:
    life=3
    def attack(self):
           self.life-=1
           print("enemy reduced my life")

    def checklife(self):
          if self.life<=0:
              print("i am dead")
          else:
              print(str(self.life) +" life left")
e1=Enemy()
e2=Enemy()
e1.attack()
e1.attack()
e1.checklife()
e2.checklife()
######################################

class Dog:
    #class Atrribute
    species ='mammal'

    #initializer / instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age
#instantiate the dog object
philo=Dog("philo",5)
mikey=Dog("mikey",7)
#Access the instance variable
print("{} is {} and {} is {}.".format(philo.name,philo.age,mikey.name,mikey.age))

#is philo a mammal?
if philo.species=="mammal":
    print("{0} is a {1}!".format(philo.name,philo.species))
