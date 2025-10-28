#A.Basics: index access.

#1. creați o listă cu 5 elemente
lst = list(range(10, 15))

#2. printați lista
print(lst)

#3. printați primul element din listă
print(lst[0])

#4. printați ultimul element din listă
print(lst[-1])

#5. printați slice-ul cu elementele de la indexul 2 la indexul 4, inclusiv
print(lst[2:5])

#6. modificați al 3lea element din listă folosind assignment:
# lst[idx] = value
lst[2] = "altceva"
print(lst)

#7. încercați să schimbați un slice dintr-o listă. este posibil?
# lst[start:stop] = [....]
lst[1:3] = ["ala", "bala"]
print(lst)



import random

def operate_on(lst):
    lst.append(random.randint(1, 100))

lst = ["ala", "bala"]
operate_on(lst)

# CONCLUZIE: în Python totul este o referință

