#1. repetați string-ul "bla bli blu" de 3 ori.
"bla bli blu" * 3

#2. obțineți partea întreagă a împărțirii lui 17 la 4.
17 // 4
int(17 / 4)

#3. obțineți restul împărțirii lui 17 la 4.

17 % 4


#4. setați variabilele
name = "Jane"
is_student = True

# scrieți o condițională care pe un branch să facă print
# la "Jane is a student", pe cealaltă la
# "Jane is not a student".

# schimbați apoi variabilele în
name = "Andrew"
is_student = False

# și rulați din nou.

if is_student:
    print(name + " is a student")
else:
    print(name + " is not a student")


#5. dat fiind stringul
s = "Bună dimineața"

# - verificați pe ce poziția apare substringul "dimi"
s.index("dimi")
s.find("dimi")

# - verificați dacă se termină cu "ta"
s.endswith("ta")

# - verificați dacă începe cu "Bu"
s.startswith("Bu")

# - aflați lungimea string-ului folosind funcția `len()`
len(s)


#6. dat fiind stringul
s = "===Column Header==="
# extrageți numele coloanei fără caracterele "="
s.strip("=")

#7. dat fiind stringul
s = "Column Header"
# generați un string nou cu lungime de 25 de caractere
# pad-uit la stânga și la dreapta cu caracterul "#".

maxchars = 16
len_s = len(s)

if len_s < maxchars:
    extra_chars = maxchars - len_s
    pad_left_chars = extra_chars // 2
    pad_right_chars = extra_chars - pad_left_chars

    print(
        '#' * pad_left_chars + s + '#' * pad_right_chars
    )

# sau...
s.center(25, "#")


#8. scrieți o funcție `cube(x)` ce calculează x la puterea a 3a

def cube(x):
    return x ** 3

#9. luați un număr întreg ca input de la utilizator,
#   folosiți funcția `cube()`, și faceți print cu textul:
#   "Cubul numărului <număr> este <cub>."

n = int(input("Un număr: "))
print("Cubul numărului %s este %s." % (n, cube(n)))



#10. scrieți o funcție
def count_appearances(substr, txt):
    substr = substr.casefold()
    txt = txt.casefold()

    return txt.count(substr)

def count_appearances(substr, txt):
    return txt.casefold().count(substr.casefold())


# ce numără de câte ori apare `substr` în `txt`, case-insensitive.

count_appearances("bu", "Bucureștiul este bun") == 2
count_appearances("BU", "Bucureștiul este bun") == 2