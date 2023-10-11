'''
In Python, a class method is a method that is bound to the class and not the instance of the class. 
It can't modify object state (instance-specific data) but can modify class state (class-specific data). You define a class method using the @classmethod decorator.
'''

class MyClass:
    
    class_var = "I'm a class variable"
    
    @classmethod
    def my_class_method(cls):
        return cls.class_var

# Calling class method using the class itself
print(MyClass.my_class_method())  # Output: I'm a class variable

# Calling class method using an instance of the class
obj = MyClass()
print(obj.my_class_method())     # Output: I'm a class variable
