'''
In python we have iterators, both generators and iterables. 
'''

# Generators generate the output once 
generator = (word + '!' for word in 'generating generic generations generator'.split())

#We generate the first time 
for value in generator:
    print(value)

#Second time the generator is empty 
for value in generator: 
    print(value)


# Iterables generate output several times
class GenericIterable(object): 

    def __iter__(self):

        for word in 'generating generic generations generator'.split():
            yield word + '!'

iterable = GenericIterable()

# First time the iterable yields values
for value in iterable:
    print(value)

# The iterable still yields values the second time
for value in iterable: 
    print(value)