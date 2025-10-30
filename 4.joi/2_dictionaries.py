# dictionaries

# o structură de date simplă
# ce asociază o valoare unei chei.
# (și este o colecție de astfel de perechi cheie-valoare)


d = {
    'name': 'Jane',
    'age': 25,
    'is_student': False,
}

d = {
    1: "v1",
    2: "v2",
}

d[2] = "valoare modificată"
d[3] = "altă valoare"

print(d['name'])

# dat fiind datasetul "data/users.json",
# încărcați-l din fișier într-o variabilă "data"

# utilizăm json.load(fp)

import json

with open("data/users.json", encoding='utf-8') as fp:
    data = json.load(fp)
    print(data)

# Exercițiu:
#
# folosind `data` de mai sus,
# creați o listă cu persoanele (adică dicționarele)
# cu vârsta mai mare de 40 de ani


with open("data/users.json", encoding='utf-8') as fp:
    data = json.load(fp)

    filtered = []
    for person in data:
        #print(person)
        age = person['age']
        if age > 40:
            filtered.append(person)

    print(filtered)

print([
    person for person in data if person['age'] > 40
])


# Exercițiu:
#
# folosind `data` de mai sus,
# creați o listă cu numele utilizatorilor.
#
# dacă utilizatorul nu are nume,
# considerați numele combinația dintre
# first_name și last_name,
# și dacă nici acestea nu există,
# e-mail-ul

#
# pentru a verifica dacă există o cheie
# într-un dicționar folosiți operatorul "in"

names = []
for person in data:
    if 'name' in person:
        name = person['name']
    else:
        try:
            name = "%s %s" % (person['first_name'],
                            person['last_name'])
        except KeyError:
            name = person['email']

    names.append(name)

print(names)


# Exercițiu:
# scrieți o funcție `get_actives(dataset)`
# ce chemată cu structura de date de mai sus,
#
# consideră pe cineva activ dacă "is_active": True,
# sau dacă nu este setat.
#
# folosiți metoda .get() a dicționarului

print(d.get('is_active', True))

def get_actives(dataset):
    return [
        person
        for person in dataset
        if person.get("is_active", True)
    ]

print(get_actives(data))



d = {
  "București": 0,
  "Iași": 340,
  "Cluj": 520,
  "Timișoara": 620,
}

# dicționarul iterează pe cheie
for elem in d:
    print(elem)

# iterație pe cheie și valoare, deodată
for k, v in d.items():
    print(k, '::', v)
