class Mammal:
    def walk():
        print('walk')

#inheritance (Mammal) inside another class
class Dog(Mammal):
    pass


class Cat(Mammal):
    pass

c=Cat

c.walk()
d=Dog
d.walk()
