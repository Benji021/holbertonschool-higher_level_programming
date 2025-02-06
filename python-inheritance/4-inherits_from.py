#!/usr/bin/python3
""" Function to check if an object is an instance of 
a class that inherited from a specified class """


def inherits_from(obj, a_class):
    """Check if obj is an instance of a subclass of a_class (but not a direct instance of a_class).
    
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    
    Returns:
        bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

# Tests
class A:
    pass

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

print(inherits_from(b, A))  # Doit afficher True
print(inherits_from(c, A))  # Doit afficher True
print(inherits_from(a, A))  # Doit afficher False
print(inherits_from(b, B))  # Doit afficher False