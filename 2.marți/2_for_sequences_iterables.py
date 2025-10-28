# dată fiind tupla
t = ("Jane", 45)

# obțineți din ea variabilele `name` și `age`
name = t[0]
age = t[1]

# dat fiind
MIN_AGE = 25

# și lista de tuple

l = [
    ("Jane", 45),
    ("Jay", 12),
    ("Robert", 18),
    ("Andrew", 28),
    ("Mary", 33),
]

# iterați în listă
# și printați un string de forma:
# "<name> is old enough"
# sau 
# "<name> is not old enough"

for elem in l:
    name = elem[0]
    age = elem[1]
    if age >= MIN_AGE:
        print(name + " is old enough")
    else:
        print(name + " is not old enough")


# transformați codul de mai sus într-o funcție
# ce returnează tuplele oamenilor cu vârsta potrivită

def filter_by_age(min_age, people):
    out = []

    for elem in people:
        name = elem[0]
        age = elem[1]
        if age >= min_age:
            out.append(elem)

    return out


# dată fiind o listă de oameni, în forma tuple de nume și vârstă

l = [
    ("Jane", 45),
    ("Jay", 12),
    ("Robert", 18),
    ("Andrew", 28),
    ("Mary", 33),
    ("John", 65),
    ("Luke", 72),
    ("Matthew", 42),
]

# și dat fiind
MIN_AGE = 25
MAX_AGE = 45

# creați două liste, `accepted` și `rejected``

# pattern-ul este:
#
# 1. instanțiem obiectul / obiectele
accepted = []
rejected = []

# 2. iterăm
for rec in l:
    age = rec[1]
    # 3. filtrăm
    if MIN_AGE <= age <= MAX_AGE:
      # 4. construim
      accepted.append(rec)
    else:
      rejected.append(rec)
      
print(accepted)
print(rejected)


# transformați-o într-o funcție:
def filter_by_age(min_age, max_age, people):
    # pattern-ul este:
    #
    # 1. instanțiem obiectul / obiectele
    accepted = []
    rejected = []

    # 2. iterăm
    for rec in people:
        age = rec[1]
        # 3. filtrăm
        if min_age <= age <= max_age:
            # 4. construim
            accepted.append(rec)
        else:
            rejected.append(rec)

    # 5. returnăm
    return accepted, rejected

print(
    filter_by_age(MIN_AGE, MAX_AGE, l)
)

# EXERCIȚIU:
#
# dată fiind lista de mai sus `l`
# calculați minimul și maximul vârstei


# strategie:
# inițializăm o variabilă ce va ține valoarea maximă / minimă,
# și o updatăm la fiecare iterație după cum este nevoie

import math

min = math.inf
max = 0
# iterăm
for item in l:
    age = item[1]
    # dacă vârsta curentă este mai mare
    # decât vechiul maxim
    if age > max:
        # updatăm maximul
        max = age
    # dacă vârsta curentă este mai mică
    # decât vechiul minim
    if age < min:
        # updatăm minimul
        min = age
        
print(min, max)

# Q: ^^ de câte ori parcurge lista?
# A: o dată

# Q: folosește pentru memorie o listă adițională?
# A: nu


# EXERCIȚIU:
#
# repetați exercițiul de mai sus, folosind
# built-in-urile `min()` și `max()`

# strategie:
# creăm o listă de vârste
varste = []

for item in l:
    age = item[1]
    varste.append(age)
print(varste)

min(varste)
max(varste)

# Q: ^^ de câte ori parcurge lista?
# A: 3

# Q: folosește pentru memorie o listă adițională?
# A: da


### building a list ###
# EXERCIȚIU:
# creați o listă cu vârstele între MIN_AGE și MAX_AGE

people = [
    ("Jane", 45),
    ("Jay", 12),
    ("Robert", 18),
    ("Andrew", 28),
    ("Mary", 33),
    ("John", 65),
    ("Luke", 72),
    ("Matthew", 42),
]

# the regular way:
# we initialize
ages = []
# we iterate over the source
for item in people:
    # we verify:
    if MIN_AGE <= item[1] <= MAX_AGE:
        # we append
        ages.append(item[1])

# with list comprehension:
[
    item[1]
    for item in people
    if MIN_AGE <= item[1] <= MAX_AGE
]


# with generators
min([
    item[1]
    for item in people
    if MIN_AGE <= item[1] <= MAX_AGE
])

max(
    item[1]
    for item in people
    if MIN_AGE <= item[1] <= MAX_AGE
)

# nu putem calcula media pe ceva filtrat cu generatori
sum(
    item[1]
    for item in people
) / len(people)



# EXERCIȚIU
# scrieți o funcție

def filter_and_agg_by_age(min_age, max_age, people):
    pass

# și returnează o tuplă formată din:
# - lista de oameni filtrați
# - minimul vârstei acestora
# - maximul vârstei acestora
# - media vârstei acestora.

# faceți asta iterând o singură dată prin setul de date


# exemplu de rezultat:
# (
#   [('Mary', 33), ('Jane', 45)],
#   33,
#   45,
#   39
# )


def filter_and_agg_by_age(min_age, max_age, people):
    filtered = []

    min = math.inf
    max = 0
    sum = 0

    # iterăm
    for item in l:
        age = item[1]

        # filtrăm
        # if not of appropriate age, move to next
        if age < min_age or age > max_age:
            continue

        filtered.append(item)

        if age > max:
            max = age

        if age < min:
            min = age

        sum += age

    return (
        filtered, min, max, sum / len(filtered)
    )


filter_and_agg_by_age(MIN_AGE, MAX_AGE, people)


# for, break, continue
for elem in range(10):
    # dacă este impar, continue
    if elem % 2 == 1:
        continue
    # else print
    print(elem)


for elem in range(10):
    # dacă ajung la numărul 7,
    # întrerupe iterația
    if elem == 7:
        break
    print(elem)
