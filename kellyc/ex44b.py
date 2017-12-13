# Inheritance Versus Composition
# Three ways parent and child classes interact 1) actions on the child imply an action on the parent 2) actions on the child override the action on the parent 3) actions on the child alter the action on the parent

# This here is an example of overriding explicitly

# create class parent that is a class object
class Parent(object):
    # create override function to applies to self, print sumpin when invoked
    def override(self):
        print("PARENT override()")

class Child(Parent):
    # def override function that applies to self and print when invoked
    def override(self):
        print("CHILD override()")

# assign variables to classes
dad = Parent()
son = Child()

# run functions against what's been assigned to variables
dad.override()
son.override()
