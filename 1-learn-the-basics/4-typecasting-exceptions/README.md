# Typecasting

The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion: Implicit and Explicit.

- Implicit Conversion - automatic type conversion
- Explicit Conversion - manual type conversion

## Implicit Type Conversion

In certain situations, Python automatically converts one data type to another. This is known as implicit type conversion.

In the script [integer-to-float](./scripts/integer-to-float.py) Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.

Output of [integer-to-float](./scripts/integer-to-float.py):

```
Value: 124.23
Data Type: <class 'float'>
```

Observations:

- We get TypeError, if we try to add str and int. For example, '12' + 23. Python is not able to use Implicit Conversion in such conditions.
- Python has a solution for these types of situations which is known as Explicit Conversion.

## Explicit Type Conversion

In Explicit Type Conversion, users convert the data type of an object to required data type.

We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.

This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

In the script [explicit-conversion](./scripts/explicit-conversion.py) there is an example of addition of string and integer using explicit conversion.

Output of [explicit-conversion](./scripts/explicit-conversion.py):

```
Data type of num_string before Type Casting: <class 'str'>
Data type of num_string after Type Casting: <class 'int'>
Sum: 35
Data type of num_sum: <class 'int'>
```

## Key Points to Remember

- Type Conversion is the conversion of an object from one data type to another data type.
- Implicit Type Conversion is automatically performed by the Python interpreter.
- Python avoids the loss of data in Implicit Type Conversion.
  Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
- In Type Casting, loss of data may occur as we enforce the object to a specific data type.

# Exceptions

A Python program stops running immediately when it hits an error. These errors in Python can either be syntax errors or exceptions.

## Understanding Exceptions and Syntax Errors

Syntax errors occur when the parser identifies an incorrect statement. Consider the following example:

```
>>> print(0 / 0))
  File "<stdin>", line 1
    print(0 / 0))
                ^
SyntaxError: unmatched ')'
```

The arrow shows where the parser encountered the **syntax error**. Furthermore, the error message provides a clue about what went wrong. In this case, there was an extra bracket. Remove it and try running your code again:

```
>>> print(0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

This time, you encountered an **exception error**. This type of error occurs when syntactically correct Python code produces an error. The last line of the message specifies the type of exception error you encountered.

Instead of simply stating `exception error`, Python specifies the type of exception it encountered. In this instance, it was a `ZeroDivisionError`. Python includes [various built-in exceptions](https://docs.python.org/3/library/exceptions.html) and also allows for the creation of user-defined exceptions.

## Raising an Exception in Python

In certain situations, you may want to halt your program by raising an exception when a specific condition arises. You can achieve this using the `raise` keyword.

You can even complement the statement with a custom message. Imagine you are creating a small program that only accepts numbers up to 5. You can raise an error when an invalid condition occurs:

```
number = 10
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)
```

In the code above, an `Exception` object is raised with an informative custom message. The message is constructed using an f-string and a self-documenting expression.

When you run the code, you'll see the following output:

```
Traceback (most recent call last):
  File "./main.py", line 3, in <module>
    raise Exception(f"The number should not exceed 5. ({number=})")
Exception: The number should not exceed 5. (number=10)
```

The program stops and displays the exception in your [terminal](https://realpython.com/terminal-commands/) or [REPL](https://realpython.com/python-repl/), providing useful information about what went wrong. Notice that the final call to `print()` was never executed, as Python raised the exception before reaching that line of code.

Using the `raise` keyword, you can raise any exception object in Python, halting your program when an undesirable condition occurs.

# Handling Exceptions With the try and except Block

In Python, the try-except block is used to capture and manage exceptions. The code within the try block is executed normally by Python. The statements within the except block define how the program should react to any exceptions that occurred within the preceding try block.

```
try:
  print('your code here')
except:
  print('execute this when there is a exception')
```

As mentioned previously, when Python encounters an error in syntactically correct code, it raises an exception. If unhandled, this exception can cause the program to terminate abruptly. The except clause allows you to specify how your program should react when such exceptions occur.

In the script [linux_interaction.py](./scripts/linux_interaction.py), it demonstrates the usage of the try and except block.

# References and credits

The texts contained in the markdowns were obtained from the following sites:

- [programiz](https://www.programiz.com/python-programming/type-conversion-and-casting)

- [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
