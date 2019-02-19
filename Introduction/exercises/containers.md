# Containers exercise
Create a new Python script file, call it `containers.py` that contains the following lines of code
```python
a = {1: 'one', 2: 'two', 3: 'three'}
b = [1, 4, 3, 5, 7, 2, 6,]
c = (1, 2, 3, 4, 5, 6, 7,)
```
Add code to the end of this file to fulfil each of the following tasks.

1. For each of `a`, `b`, and `c`, print "`<variable> is a <type>`", where `<variable>` is "a", "b", or "c", and `<type>` is one of list, dictionary, and tuple.
2. Extend the list so that it contains the numbers 7, 8, and 9.
3. Create a new list that contains the square of each of the elements in `c`, save this list to the variable `d`.
4. A list `my_list` can be sorted using the `sort` method by writing `my_list.sort()`. Sort the list into *descending* order. (Use `help(list.sort)` if you don't see how to do this.) Print the resulting list.
5. Print the value from the dictionary that corresponds to `d[-1] % d[3]`.
