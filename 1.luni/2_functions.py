# input()
# 
# prompt = "ce faci? "
# input(prompt) # un argument opțional

# print()
# print(1, 2)
# print("multe", "chestii", "și povești") # oricâte argumente

def numefunctie(): # statement inițial cu 2 puncte
    # nivel indentat
    print("aici logica funcției")


def add(x, y):
    result = x + y

    return result # pot să capturez acest rezultat


# scrieți o funcție `feet_to_meters()`
# 1 m = 3.28084 ft

M_TO_FT = 3.28084

def feet_to_meters(ft):
    m = ft / M_TO_FT
    return m

def meters_to_feet(m):
    ft = m * M_TO_FT
    return ft

meters_to_feet(2) == 6.56168
feet_to_meters(6.56168) == 2


# scrieți o funcție ce primește ca argument un numărul de minute
# și returnează un string formatat astfel
# ore:minute

# testați funcția pe numere între între 0 și 1440.


def format_minutes(total_mins):
    # total_mins = număr de minute
    # aflăm numărul de ore. cum?
    hours = int(total_mins / 60)

    # aflăm minutele rămase
    mins = total_mins - (hours * 60)


    # soluția 1:
    # dacă minutele au un singur caracter
    if mins < 10:
        # îi punem un zero în față
        mins = "0" + str(mins)

    output = "%s:%s" % (hours, mins)

    # soluția 2:
    # folosim metoda zfill a str-ului
    output = "%s:%s" % (hours, str(mins).zfill(2))

    # soluția 3:
    # facem formatare direct în string substitution
    output = "%i:%02i" % (hours, mins)


    return output


format_minutes(59) == "0:59"
format_minutes(139) == "2:19"



