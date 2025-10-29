# dată fiind structura de date

people = [
    ("Jane", 20, ["reading", "hiking", "biking"]),
    ("Mike", 17, ["hiking", "fishing"]),
    ("Anna", 25, []),
    ("Sam", 40, ["playing guitar"]),
    ("Dan", 34, ["painting", "reading"]),
]

# Exercițiu 1: accessați și printați:
# - primul element din listă
print( people[0] )

# - penultimul element din listă
print( people[-2] )

# - vârsta penultimului element din listă
print( people[-2][1] )

# - primul hobby al primului element din listă
print( people[0][2][0] )

# - folosind sintaxa de slice, penultimele 2 elemente din listă
print( people[-2:] )

# - primele 2 hobby-uri ale primului element
print( people[0][2][:2] )


# Exercițiu 2: scrieți o funcție
def search_by_name(name, lst):
    pass
# ce returnează tupla (name, age, hobbies) conformă numelui dat

def search_by_name(name, lst):
    for item in lst:
        if item[0] == name:
            return item

search_by_name("Anna", people) == ("Anna", 25, [])

# strategie:
# 1. for pe `lst`
# 2. o condiție --> dacă da, întoarcem (returnăm / facem break și returnăm)
#               --> dacă nu, continuăm for


# Exercițiu 3: scrieți o funcție
def filter_by_age(min_age, lst):
    pass
# ce returnează o listă cu tuplele tututor persoanelor
# cu vârsta mai mare decât `min_age`

def filter_by_age(min_age, people):
    # inițializez
    persons = []

    # iterez
    for person in people:
        # filtrez
        if person[1] > min_age:
            # construiesc
            persons.append(person)

    # returnez
    return persons

# 3.1.: îl faceți și cu list comprehension?

def filter_by_age(min_age, people):
    return [
        person
        for person in people
        if person[1] > min_age
    ]


# Exercițiu 4:
# folosind funcția `search_by_name()`:
# - ștergeți-i lui Jane hobby-ul "biking"
#   (atenție, vă prefaceți că nu știți pe ce poziție este "biking")
#   --> .remove()
# - adăugați-i lui Sam hobby-urile ["knitting", "halbere"]
#   --> .extend()
# - ștergeți-i lui Dan toate hobby-urile
#   --> .clear()
#

search_by_name("Jane", people)[2].remove("biking")
search_by_name("Sam", people)[2].extend(["knitting", "halbere"])
search_by_name("Dan", people)[2].clear()

# după aceste operațiuni, inspectați lista inițială people

# concluzie: totul este o referință.
#            noi am acționat asupra structurii de date inițiale.


# Exercițiu 5:
# folosind funcția `filter_by_age()`,
# adăugați tuturor persoanelor cu vârsta mai mare de 30 de ani
# hobby-ul "knitting"

for person in filter_by_age(30, people):
    person[2].append("knitting")


print("""
    Principle of least astonishment.
""")
# "princpiu de common-sense"
