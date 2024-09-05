from dataclasses import dataclass

# working with classes using the dataclass library

# creating a class
@dataclass
# notice (self) in basic python classes are not included in the dataclass
class Student:
    name: str
    school_id: str
    GPA: float

    # overwrites the default string display to display your own formatted string when code is ran
    def __str__(self):
        return f'Name: {self.name}, School ID: {self.school_id}, GPA: {self.GPA}'


# creating Student Objects and printing them
def main():
    alex = Student('Alex', 'abcdef', 3.4)

    print(alex)

    sam = Student('Sam', 'qwerty', 2.8)
    print(sam)

    sarah = Student('Sarah', 'asfsfs', 4.0)

    ann = Student('Ann', 'sfsfssdf', 3.7)

    print(sarah)
    print(ann)

main() # make sure this is at the bottom of every python file that has a main function


# part 3 - In my opinion, working with dataclasses is a bit more simple when creating instance variables as opposed to
# with regular classes you have to create an initializer with a function and parameters and instance variables...
# dataclasses creates a simpler way to display data to the user with legible code unless you overwrite the type of string you'd
# like to print whereas in regular classes you'll output something unreadable and it might be a bit difficult to figure out
# why output is not legible