# About conditionals

Conditional Statements in Python perform different actions depending on whether a specific condition evaluates to true or false. Conditional Statements are handled by IF-ELIF-ELSE statements and MATCH-CASE statements in Python.

# <strong>The if, elif and else statements</strong>

Python if Statement is used for decision-making operations. It contains a body of code which runs only when the condition given in the if statement is true. If the condition is false, then the optional else statement runs which contains some code for the else condition.

When you want to justify one condition while the other condition is not true, then you use Python if else statement.

In the script [if-elif-else](if-elif-else.py) there are examples of the use of `if`, `elif` and `else` statements.

Output of [if-elif-else](if-elif-else.py):

```
Enter x value: 10
Enter y value: 20
x is less than y
```

# <strong> The match case statement </strong>

The pattern matching process takes as input a pattern (following case) and a subject value (following match). Phrases to describe the process include “the pattern is matched with (or against) the subject value” and “we match the pattern against (or with) the subject value”.

The primary outcome of pattern matching is success or failure. In case of success we may say “the pattern succeeds”, “the match succeeds”, or “the pattern matches the subject value”.

In many cases a pattern contains subpatterns, and success or failure is determined by the success or failure of matching those subpatterns against the value (e.g., for OR patterns) or against parts of the value (e.g., for sequence patterns). This process typically processes the subpatterns from left to right until the overall outcome is determined. E.g., an OR pattern succeeds at the first succeeding subpattern, while a sequence patterns fails at the first failing subpattern.

A secondary outcome of pattern matching may be one or more name bindings. We may say “the pattern binds a value to a name”. When subpatterns tried until the first success, only the bindings due to the successful subpattern are valid; when trying until the first failure, the bindings are merged. Several more rules, explained below, apply to these cases.

In the script [match](match.py) there's an example of the use of `match` statement. Output of the script:

```
Number
List, tuple, or set
```

# References and credits

The texts contained in the markdowns were obtained from the following sites:

- [guru99](https://www.guru99.com/if-loop-python-conditional-structures.html)
- [datagy.io](https://datagy.io/python-switch-case/)
- [PEP 634 – Structural Pattern Matching: Specification](https://peps.python.org/pep-0634/)
