import random

def sameOwner():
        Cat1= Cat("cat1","olek","red","moew")
        Dog1= Dog("togo","oleks","brown","wof")
        if Cat1.owner==Dog1.owner:
            print "owner is the same"
        else:
            print "owner is diffrent"
            print ""


   
def findOldest(pets):
    print"Test"
    maxi=0
    for i in pets:
        #print i.age,"testing age"
        if i.age>maxi:
            maxi=i.age
            OldOwner = i.owner
            position= 0
            name=i.name
    print "The oldest pet is pets[",position,"]"
    print "Owner of the oldest animal is",OldOwner
    print "the name of he oldest animal is ",name
    print"Oldest pet has got",maxi,"years."
        
    

 
            
        
 

#part 1
            
            #code is more clear than part1 and use 'direct passing' values when appropiate
class Pet:
        owner=""
        name=""
      
        def  __init__(self,name,owner):
             self.name=name
             self.owner=owner
             self.sound=""
             self.age=random.randint(1,7)

        def set_age():
            
            print""

        def set_name(self,new_name):
             self.name=new_name
             
        def get_name(self):
            return self.name
        
        def set_owner(self,owner):
             self.owner=owner   

        def get_owner(self):
            return self.owner

        def speak(self):
            return self.sound
        
        def set_sound(self,new_sound):
            self.sound=new_sound
             
        def show(self):
            print self.get_name()
            print self.get_owner()
            print self.speak()

        def __gt__ (self,other):
            return self.age>other.age

        def __lt__ (self,other):
            return self.age<other.age

        def __eq__ (self,other):
            
            return self.age==other.age 
        
            
class Dog(Pet):
        
    colour=""

    def __init__(self,new_name,new_owner,new_colour):
        Pet.__init__(self,new_name,new_owner)
        self.colour=new_colour
        self.set_sound("Woof")

    def set_colour(self,colour):
        self.colour=colour

    def get_colour(self):
        return self.colour
        
    def show(self):
        Pet.show(self)
        print self.get_colour()
        
class Cat(Pet):
        
    colour=""

    def __init__(self,new_name,new_owner,new_colour):
        Pet.__init__(self,new_name,new_owner)
        self.colour=new_colour
        self.set_sound("Meow")

    def set_colour(self,colour):
        self.colour=colour

    def get_colour(self):
        return self.colour
        
    def show(self):
        Pet.show(self)
        print self.get_colour()
        
#main
pet1=Pet("pet1","olek")
pet2=Pet("pet2","olek")
if pet1==pet2:
    print"pet1 is egual to pet2"# almost imposlible since age is random each time
else:
    print"pet1 is different than pet2"

pets =[Pet("pet0","olek"),Pet("pet1","olek"),Pet("pet2","olek"),Pet("Chapion1","Chris"),Pet("pet5","Maciek"),Pet("pet9","Olek"),Pet("pet1","ALALA"),Pet("pe181","alex")]

