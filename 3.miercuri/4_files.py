# open()

"""
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
========= ===============================================================
"""

# creați un fișier "times.txt" cu următorul conținut
"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of light, it was the season of darkness, it was the spring of hope, it was the winter of despair."

fname = "3.miercuri/times.txt"


# A. modaliteatea 1 de folosire
#    (în practică probabil nu veți face asta)

fp = open(fname)

content = fp.read()
print(content)

fp.seek(0)

for i, line in enumerate(fp):
    line = line.removesuffix("\n")
    print(i, line)

fp.close()

# B. modalitatea 2 de folosire
#    (ce veți face aproape întotdeauna)

# with deschide un "context manager"
with open(fname) as fp:
    for i, line in enumerate(fp):
        line = line.removesuffix("\n")
        print(i, line)



# Exercițiu:
# citiți conținutul fișierului "times.txt"
# și scrieți-l într-un fișier "copy.txt"

fin = "3.miercuri/times.txt"
fout = "3.miercuri/copy.txt"
with open(fin, encoding="utf-8") as fp_in, \
     open(fout, "w", encoding="utf-8") as fp_out:
    
    fp_out.write(fp_in.read())
