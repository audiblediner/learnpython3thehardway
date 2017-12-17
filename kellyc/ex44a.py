# Inheritance Versus Composition
# Three ways parent and child classes interact 1) actions on the child imply an action on the parent 2) actions on the child override the action on the parent 3) actions on the child alter the action on the parent

# This here is an example of implicit inheritance
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    # pass creates an empty block, saying you wanna make a class Child that inherits from Parent but you don't wanna tawk more about it right nah
    # if you change Parent to object and run the below, it complains that 'child' object has no att 'implicit'
    pass

dad = Parent()
son = Child()

# Note what happens when you run this
# SPOILER: the print statement above prints "PARENT implicit()" (wow?) twice (oh)
dad.implicit()
son.implicit()
