class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am {0}!".format(self.name))

new_name = input()
new_person = Person(new_name)
new_person.greet()