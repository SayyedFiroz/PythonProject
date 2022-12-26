class Computer:

    def __init__(self):                             # self parameter is a reference to the current instance of the class,
                                                    # and is used to access variables that belongs to the class.
        self.name = "Firoz"
        self.age = 19

    def update(self):                               # Self is pointer to the object
        self.age = 21

    def compare(self, other):                       # Compare(who is calling,whom to compare)
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()                                     # Constructor allocate size to object
c2 = Computer()

c1.age = 21

if c1.compare(c2):
    print("They are same")
else:
    print("They are Different")

print(c1.name)
print(c2.name)
