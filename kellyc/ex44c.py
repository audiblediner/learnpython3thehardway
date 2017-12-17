# Inheritance Versus Composition
# Three ways parent and child classes interact 1) actions on the child imply an action on the parent 2) actions on the child override the action on the parent 3) actions on the child alter the action on the parent

# make a class Parent that inherits from the class object
class Parent(object):
    # def function altered to apply to self
    def altered(self):
        print("PARENT altered()")


# make a class child that inherits from the class parent
class Child(Parent):

    def altered(self):
        # at this point, altered has just been applied to the child class
        print("CHILD, BEFORE PARENT altered()")
        # call super with arguments CHILD and self, then call the function
        # altered on whatever returns
        # here, call super with arguments Child and self , then call the function altered on whatever it returns
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
