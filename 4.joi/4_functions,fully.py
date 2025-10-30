# functions.py

# argument packing and unpacking.
# variable positional arguments.

def func(arg1, arg2, *args):
    print("arg1:", arg1)
    print("arg2:", arg2)
    
    print("args is:", args)

lst = ["ala", "bala", "porto", "cala"]

func(*lst)


# variable keyword arguments.
dict(k1=20, k2=30)

"vârsta lui {name} este {age}".format(age=20, name="Jane")


def func(a, b, *args, kw1=None, kw2=None, **kwargs):
    print("     a :", a)
    print("     b :", b)
    print("  args :", args)
    print("   kw1 :", kw1)
    print("   kw2 :", kw2)
    print("kwargs :", kwargs)

func("x", "y", "z", "țț")

func("x", "y", "z", "țț", nume="Jane", age=30)

