#Day 15

print("List Methods")

method = ['append','clear','copy','count','extend','index','insert','pop','remove','reserve','sort']
description = list(('Adds an element at the end of the list','Removes all the elements from the list','Returns a copy of the list','Returns the number of elements with the specified value','Add the elements of a list (or any iterable), to the end of the current list','Returns the index of the first element with the specified value','Adds an element at the specified position','Removes the element at the specified position','Removes the first item with the specified value','Reverses the order of the list','Sorts the list'))

for method, description in zip(method, description):
    print(f'Method {method}() --> {description}')