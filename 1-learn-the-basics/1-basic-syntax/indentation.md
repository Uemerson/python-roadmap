# About Python indentation

Python provides no braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.

# Examples

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example:

```
if True:
    print("Correct Indentation")
else:
    print("Correct Indentation")

print("Keeping correct Indentation")
```

However, the following block generates an error:

```
if True:
print("Incorrect Indentation")
else:
print("Incorrect Indentation")

print("Keeping incorrect Indentation")
```

# References

- [tutorialspoint](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
