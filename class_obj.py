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
    
#########################################

class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
#c1.attr

##########################################

#store marks of 3 subject of student in a list through class
class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("enter the marks of %s student in subject %d"%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
s1=student("Anshul")
s1.entermarks()
s2=student("Thor")
s2.entermarks()
s1.display()
s2.display()
##############################################
                
#keep track of number of employees
class employee:
    empc=0
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
        employee.empc=employee.empc+1
    def displaydetails(self):
        print("name=",self.name,"designation=",self.designation,"salary=",self.salary)
    def empcount(self):
        print("there are %d Employees"%employee.empc)

e1=employee("Rohit","SE",1300000)
e2=employee("RohitMittal","Developer",1700000)
e1.displaydetails()
e2.displaydetails()
e1.empcount()
