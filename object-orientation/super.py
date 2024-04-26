## Calling a method from a superclass with multiple inheritance. 


class A:
    def some_method(self):
        print("A's method")

class B(A):
    def some_method(self):
        print("B's method")
        super().some_method()

class C(A):
    def some_method(self):
        print("C's method")
        super().some_method()

class D(B, C):
    def some_method(self):
        print("D's method")
        super().some_method()

d = D()
d.some_method()