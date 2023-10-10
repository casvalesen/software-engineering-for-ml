from collections import Counter 

words = ['fly', 'bee', 'wasp', 'bee']

word_count = Counter(words)
print(word_count)


# elements(): Returns an iterator over the elements in the Counter, repeating as many times as the count:
c = Counter(a=3, b=2, c=1)
print(list(c.elements()))

# most_common([n]): Returns a list of the n most common elements and their counts, from the most common to the least:
print(word_count.most_common(2))  # Output: [('bee', 2), ('fly', 1)]


# subtract([iterable-or-mapping]): Subtract elements from an iterable or another mapping:

c = Counter(a=3, b=2, c=1)
d = Counter(a=1, b=1, c=2)
c.subtract(d)
print(f'c subtract d is {c}') 


# +, -, &, |: Counter objects support arithmetic operations to combine tallies:

c = Counter(a=3, b=2, c=1)
d = Counter(a=1, b=1, c=2)
print(c + d)  # addition:  c[x] + d[x]
print(c - d)  # subtraction: c[x] - d[x]
print(c & d)  # intersection:  min(c[x], d[x])
print(c | d)  # union:  max(c[x], d[x])

# A Counter object is already a dictionary-like object, but if you need to convert it to a pure dictionary, you can use the dict() constructor:

word_count_dict = dict(word_count)
print(word_count_dict)  
#You can update a Counter object with new data:
word_count.update(["bee", "butterfly"])
print(word_count)  
