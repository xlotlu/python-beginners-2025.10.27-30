# Ex. 1:
# citiți docstring-ul funcției `open`,
# și scrieți-l într-un fișier "open_doc.txt".
#
# docstring-ul se accesează cu atributul `__doc__`

with open("open_doc.txt", 'w', encoding="utf-8") as f:
    f.write(open.__doc__)


# Ex. 2:
# scrieți o funcție `grep(pattern, fname)`
# ce printează fiecare linie din fișierul `fname`
# ce conține `pattern`

def grep(pattern, fname):
    with open(fname, encoding="utf-8") as f:
        for line in f:
            if pattern in line:
                print(line)

# Ex. 2.1: transformați funcția să returneze
# o listă de stringuri (liniile care fac match)

def grep(pattern, fname):
    matches = []

    with open(fname, encoding="utf-8") as f:
        for line in f:
            if pattern in line:
                matches.append(line)

    return matches



# Ex. 2.2: cu list comprehension?

def grep(pattern, fname):
    with open(fname, encoding="utf-8") as f:
        return [
            line
            for line in f
            if pattern in line
        ]

# Ex. 3:
# scrieți o funcție `cp(source, target, overwrite=False)`
# ce copiază conținutul fișierului `source`
# în `target`.
#
# 1. faceți funcția să refuze overwrite
#    dacă parametrul opțional `overwrite` nu e True.
# 2. faceți-o să funcțieze și cu fișiere binare.
# 3. vă puneți întrebarea:
#    ce se întâmplă cu un fișier de 12GB?

def cp(source, target, overwrite=False):
    if overwrite:
        mode = "wb"
    else:
        mode = "xb"

    with open(source, "rb") as inf, open(target, mode) as outf:
        outf.write(
            inf.read()
        )

# Ex. 3.1:
# Q: cum optimizăm alocarea memoriei?
# A: chunking

def cp(source, target, overwrite=False):
    if overwrite:
        mode = "wb"
    else:
        mode = "xb"

    with open(source, "rb") as infp, open(target, mode) as outfp:
        chunk_size = 4096

        while True:
            data = infp.read(chunk_size)

            if not data:
                break

            outfp.write(data)


def cp(source, target, overwrite=False, chunk_size=4096):
    with open(source, "rb") as infp, \
         open(target, "wb" if overwrite else "xb") as outfp:
        
        while data := infp.read(chunk_size):
            outfp.write(data)






