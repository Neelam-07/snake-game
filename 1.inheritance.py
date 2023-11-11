
#inheritance: inheriting attributes and the methods from a class and using it to another class.

class Animal:
    def __init__(self):
        self.num_0f_eyes= 2

    def breathe(self):
        print("inhale or exhale")


#inheriting the animal class to the fish class 
class Fish(Animal):
    def __init__(self):
        super().__init__()   #leave the init empty

    def swim(self):
        print("moving under water")

nemo = Fish()
nemo.breathe()
nemo.swim()

#if u want to add another attribute to the breathe method then
class Fish(Animal):
    def __init__(self):
        super().__init__()   #leave the init empty

    def breathe(self):    #want to add one more method in breathe method from super class 
        super().breathe()   #get super class method using the super().whatevr_the_method_is
        print("doing this under water")

    def swim(self):
        print("moving under water")

nemo = Fish()
nemo.breathe()
nemo.swim()