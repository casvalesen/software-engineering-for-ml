# Basic 

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2
    

c = Circle(5)
print(c.diameter)

# For getters and setters
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:  # Ensure name isn't empty or None
            raise ValueError("Name cannot be empty")
        self._name = value


p = Person('Bob')
print(p.name) 
p.name = 'Bob Iger'

print(p.name)

'''
In this example, when you access name, it uses the name method with @property (i.e., the getter). 
When you assign a value to name, it uses the name method with @name.setter (i.e., the setter).

'''
