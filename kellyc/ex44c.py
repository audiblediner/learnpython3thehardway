# Inheritance Versus Composition

class Parent(object):
    
    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # call super with arguments CHILD and self, then call the function
        # altered on whatever returns
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
