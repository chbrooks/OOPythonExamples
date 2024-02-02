class Cat :

    ## we use self to identify member variables.
    def __init__(self, name=""):
        self.name = name

    ## Our base class' method
    def say_hello(self):
        print("Meow")

class TalkingCat(Cat) :
    ## Here we are overriding say_hello
    def say_hello(self):
        print("Hello my name is %s" % (self.name))

class HungryCat(Cat) :
    ## here we are extending say_hello. Since Python allows multiple inheritance,
    # we need to specify the name of the parent class whose method we want to use.
    def say_hello(self):
        Cat.say_hello(self)
        print("I am hungry")

class Dog() :
    def __init__(self, name=""):
        self.name = name
    def say_hello(self):
        print("Arf")

## Cat is the first class, so we will follow that parent first.
class CatDog(Cat, Dog) :
    pass

## Dog
# is the first class, so we will follow that parent first.

class DogCat(Dog, Cat) :
    pass

class ChattyCatDog(Dog, TalkingCat) :
    ## here we are specifying the parent to use.
    def say_hello(self):
        TalkingCat.say_hello(self)
        print("but I am a dog")

if __name__=="__main__" :

    c = Cat("katniss")
    c.say_hello()
    # c2 = TalkingCat("Obi-wan")
    # c2.say_hello()
    # c3 = HungryCat("Pixie")
    # c3.say_hello()
    # d = Dog("fluffy")
    # d.say_hello()
    # d2 = CatDog("fido")
    # d2.say_hello()
    # d3 = DogCat("rover")
    # d3.say_hello()
    # d4 = ChattyCatDog("spot")
    # d4.say_hello()