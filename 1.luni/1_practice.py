# Romania's GDP in 2022 was 284 billion euros. In the same year, Romania's population was 19.5 million. Define two variables gdp and population and store these values. Compute and display Romania's GDP per capita in 2022.

# gdp = "284 billions euros"
gdp = 284 * 10**9

# population = "19.5 millions"
population = 19.5 * 10**6

#print("2022 GDP was:", gdp / population)

print(
    "2022 GDP was: %s € per capita" % round(gdp / population, 4)
)




# 1. luați input de la utilizator pentru a afla vârsta sa
# 2. luați input de la utilizator pentru a afla vârsta prietenului
# asignați-le la 2 variabile

# calculați diferența

# și faceți-i print

your_age = input("How old are you? ")
friend_age = input("How old is your friend? ")

diff = int(your_age) - int(friend_age)

print(diff)


# cerința 2:
# dacă prietenul este mai în vârstă, print cu:
# "prietenul este mai în vârstă cu <n> ani"
# altfel:
# "tu ești mai în vârstă cu <n> ani"

your_age = 25
friend_age = 45

if your_age > friend_age:
    #print("tu ești mai în vârstă cu " + str(diff) + " ani")
    diff = your_age - friend_age
    print("tu ești mai în vârstă cu %s ani" % diff)
else:
    diff = friend_age - your_age
    print("prietenul este mai în vârstă cu %s ani" % diff)


    
diff = your_age - friend_age

if diff == 0:
    print("sunteți de aceeași vârstă")
elif diff > 0:
    print("tu ești mai în vârstă cu %s ani" % diff)
elif diff < 0:
    print("prietenul este mai în vârstă cu %s ani" % -diff)



"""
if condition1:
    logic1

elif condition2:
    logic2

elif condition3:
    logic3

...

else:
    logicx
"""


# faceți print stringului:

# aceasta este o poveste numită "povestea frumoasă de din'colo de zări"
print('aceasta este o poveste numită "povestea frumoasă de din\'colo de zări"')


print("aici\nam spart\nrândul")

print("""
liniile
sunt
păstrate
""")





