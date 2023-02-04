# Typecasting

The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion: Implicit and Explicit.

- Implicit Conversion - automatic type conversion
- Explicit Conversion - manual type conversion

# Implicit Type Conversion

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

# Explicit Type Conversion

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

# Key Points to Remember

- Type Conversion is the conversion of an object from one data type to another data type.
- Implicit Type Conversion is automatically performed by the Python interpreter.
- Python avoids the loss of data in Implicit Type Conversion.
  Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
- In Type Casting, loss of data may occur as we enforce the object to a specific data type.

# References and credits

The texts contained in the markdowns were obtained from the following sites:

- [programiz](https://www.programiz.com/python-programming/type-conversion-and-casting)
