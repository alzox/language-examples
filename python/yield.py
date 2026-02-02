"""
Python has a syntax called yield which converts a list to a specific instance of an iterator called a generator.
"""

def bad_long_list():
    num_list = []
    for i in range(1000):
        num_list.append(i)
    return num_list

def long_list():
    for i in range(1000):
        yield i
        
for num in long_list():
    print(num)