# Checking types with 'as' in Python match-case statements
def type_of(var):
    match var:
        case int() | float() as var:
            return "Number"
        case dict() as var:
            return "Dictionary"
        case list() | tuple() | set() as var:
            return "List, tuple, or set"
        case str() as var:
            return "String"
        case _:
            return "Something else"


print(type_of(3))
print(type_of({1, 2}))
