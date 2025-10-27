# date fiind posibilitățile "morning" / "noon" / "evening" / "night"

# scrieți o funcție care să primească parametrul `tod`,
# și să returneze salutarea potrivită.


def greet(tod):
    if tod == "morning" :
       greeting = 'buna dimineata'
    elif tod == "noon" :
       greeting = 'buna ziua'
    elif tod == 'evening' : 
       greeting = 'buna seara'
    elif tod == 'night': 
       greeting = 'buna noaptea'
    else:
        raise ValueError("nu există acest tod")

    return greeting


# scriem o funcție `greet_by_tod()`
# ce returnează salutul corect pentru momentul *actual* al zilei.

from datetime import datetime

def greet_by_tod():
    dt = datetime.now()

    h = dt.hour

    if 5 <= h < 11:
        tod = "Good morning"

    elif 11 <= h < 17:
        tod = "Good afternoon"

    elif 17 <= h < 21:
        tod = "Good evening"

    elif (21 <= h < 24) or (0 <= h < 5):
        tod = "Good night"

    return tod


# scrieți o funcție `greet_user()`
# fără parametri,
# ce cere numele utilizatorului,
# și îl salută cu expresia corectă.

# folosiți în interiorul funcției:
# - input()
# - funcția greet() de mai sus

# și combinați rezultatul acestora

def greet_user():
    user = input ("Care este numele tau?")
    greeting = greet_by_tod()

    # dacă vreau să chem funcția pe viitor și în alt context,
    # fac return.

    # dacă aici este funcționalitatea finală
    # (interacțiunea cu utilizatorul),
    # fac print

    # greeting + ", măi " + user
    return "%s, măi %s" % (greeting, user)


print(greet_user())

