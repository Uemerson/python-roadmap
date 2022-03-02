#   A Python identifier is a name used to identify a variable, function, class, module or other object.

#   To remember:
#   Always give the identifiers a name that makes sense. While c = 10 is a valid name, 
#   writing count = 10 would make more sense, and it would be easier to figure out what it 
#   represents when you look at your code after a long gap.

#   Multiple words can be separated using an underscore, like this_is_a_long_variable.

#   Rules for writing identifiers:
#   1. An identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters,
#   underscores and digits (0 to 9). Like:
variable = None
variable_ = None
_variable = None
variable10 = None
variable_variable = None

#   2. An identifier can be of any length.
long_name_variable = None

#   3. Python is a case sensitive programming language. Thus, Pythonpower and pythonpower 
#   are two different identifiers in Python. Like:
Pythonpower = "Pythonpower different identifiers from pythonpower"
pythonpower = "pythonpower different identifiers from Pythonpower"

#   4. Keywords cannot be used as identifiers. Like:
class = None
global = None

#   5. An identifier cannot start with a digit. Like:
0variable = None
1variable = None

#   6. Python does not allow punctuation characters such as @, $, and % within
#   identifiers. Like:
variable$ = None
variable@ = None
