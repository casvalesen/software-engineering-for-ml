def class_decorator(cls):
    class Wrapped(cls):
        def new_method(self):
            return "New method"
    return Wrapped

@class_decorator
class MyClass:
    def __init__(self, job):
        self.job = job
    def original_method(self):
        return "Original method"

