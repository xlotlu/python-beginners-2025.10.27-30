# oop

class Point:
    def __init__(self):
        print(self)

# 1. în Python, fiecare metodă a unei clase
# primește explicit ca prim argument
# instanța curentă.


# 2. semnătura clasei se pune pe metoda
# specială __init__()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 3. mai întotdeauna vrem să definim __repr__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# 4. deseori vrem să implementăm și __str__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str((self.x, self.y))


#5. first useful method

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str((self.x, self.y))
    
    def translate(self, x=0, y=0):
        self.x += x
        self.y += y


#6. don't forget to
import this


#7. something useful

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str((self.x, self.y))
    
    def translate(self, x=0, y=0):
        self.x += x
        self.y += y
        
    def get_distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)


# 8. decoratori!
from functools import cache # <-- a decorator!
from random import randint

def myfunc():
    return randint(1, 100)

@cache
def myfunc():
    return randint(1, 100)

# is equivalent to

def myfunc():
    return randint(1, 100)
myfunc = cache(myfunc)


# și în cazul nostru...

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str((self.x, self.y))
    
    def translate(self, x=0, y=0):
        self.x += x
        self.y += y
    
    @property        
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

#9. comparisons.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
    def __str__(self):
        return str(self.as_tuple())
    
    def translate(self, x=0, y=0):
        self.x += x
        self.y += y
    
    @property        
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
        
    def as_tuple(self):
        return (self.x, self.y)
        
    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()
        
    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()


#10...... and beyond (aka "deep-dive"): inheritance

class ThreeDPoint:
    def __init__(self, x, y, z):
        super().__init__(x, y) # se respectă ce face părintele

        self.z = z # ne facem treaba noastră
