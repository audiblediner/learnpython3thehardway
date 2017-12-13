# Inheritance Versus Composition
# err, this returns AttributeError: 'Child' object has no attribute 'implicit'
# moving on for now

# create class parent that inherits from class object
class Parent(object):

    # define function override to apply to self, then print statement when invoked
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(object):

    def override(self):
        print("CHILD override()")

    def implicit(self):
        print("CHILD implicit()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # call super with argument Child and self, then
        # call the function altered on what's returned
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

# call the function implicit on whatever's assigned to variables
dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
