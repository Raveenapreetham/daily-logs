
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def g(self):
        super().greet()
        print("Hello from Child")

obj = Child()
obj.g()
