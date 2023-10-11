'''
A static method in Python is a method that belongs to a class, but it doesn't require a reference to an instance or the class itself as its first parameter.
In other words, it's not tied to the class's state or the instance's state. It behaves much like a regular function, but it's defined within the context of a class and is called on the class itself or on its instances.

'''

'''
Imagine you're designing a MathHelper class which provides helper functions that don't rely on any class-specific or instance-specific data:

'''

class MathHelper:

    @staticmethod
    def square(num):
        return num * num

    @staticmethod
    def cube(num):
        return num * num * num

print(MathHelper.square(4))  # Outputs: 16
print(MathHelper.cube(3))   # Outputs: 27
