# About Variables and Data Types

Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

# Data types in Python

Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

# <strong>Python Numbers</strong>

Integers, floating point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

In the script [python-numbers](./scripts/python-numbers.py) there are examples of the use of `type()` and `isinstance()` functions. The `type()` function is used to know which class a variable or a value belongs to. The `isinstance()` function is used to check if an object belongs to a particular class.

Output of [python-numbers](./scripts/python-numbers.py):

```
10 is of type <class 'int'>
20.0 is of type <class 'float'>
(2+5j) is complex number? True
```

Integers can be of any length, it is only limited by the memory available.

A floating-point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. 1 is an integer, 1.0 is a floating-point number.

Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part. Here are some examples:

```
>>> a = 1234567890123456789
>>> a
1234567890123456789
>>> b = 0.1234567890123456789
>>> b
0.12345678901234568
>>> c = 1+2j
>>> c
(1+2j)
```

Notice that the float variable b got truncated.

# <strong>Python Strings</strong>

String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """.
Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.
The plus (+) sign is the string concatenation operator and the asterisk (\*) is the repetition operator.

In the script [python-strings](./scripts/python-strings.py) there are examples of strings. Output of the script:

```
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!We love Python ❤

Hello World!

```

# <strong>Python List</strong>

Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets `[ ]`. To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets `[ ]`.

The values stored in a list can be accessed using the slice operator `[ ]` and `[:]` with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (\*) is the repetition operator.

In the script [python-list](./scripts/python-list.py) there are examples of lists. Output of the script:

```
['abcd', 900, 3.55, 'Uemerson', 80.1]
abcd
[900, 3.55]
[3.55, 'Uemerson', 80.1]
[889, 'Uemerson', 889, 'Uemerson']
['abcd', 900, 3.55, 'Uemerson', 80.1, 889, 'Uemerson']
```

# <strong>Python Tuple</strong>

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets `[ ]` and their elements and size can be changed, while tuples are enclosed in parentheses `( )` and cannot be updated. Tuples can be thought of as read-only lists.
In the file [python-tuple](./scripts/python-tuple.py) there are examples of tuples. Output of the script:

```
('abcd', 900, 3.55, 'Uemerson', 80.1)
abcd
(900, 3.55)
(3.55, 'Uemerson', 80.1)
(889, 'Uemerson', 889, 'Uemerson')
('abcd', 900, 3.55, 'Uemerson', 80.1, 889, 'Uemerson')
```

# <strong>Python Dictionary</strong>

Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces `{ }` and values can be assigned and accessed using square braces `[]`.

In the file [python-dictionary](./scripts/python-dictionary.py) there are examples of tuples. Output of the script:

```
This is one
This is two
{'name': 'Uemerson', 'code': 6734, 'dept': 'sales'}
dict_keys(['name', 'code', 'dept'])
dict_values(['Uemerson', 6734, 'sales'])
```

Dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order". They are simply unordered.

# References and credits

The texts contained in the markdowns were obtained from the following sites:

- [tutorialspoint](https://www.tutorialspoint.com/python/python_variable_types.htm)

- [programiz](https://www.programiz.com/python-programming/variables-datatypes)
