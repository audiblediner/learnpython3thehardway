# Inheritance Versus Composition


# This here is an example of implicit inheritance
class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")
        
class Child(Parent):
    # pass creates an empty block, saying you wanna make a class but you don't
    # wanna tawk about it right nah
    pass

dad = Parent()
son = Child()

# Note what happens when you run this
# SPOILER: the print statement above prints (wow?) twice (oh)
dad.implicit()
son.implicit()



