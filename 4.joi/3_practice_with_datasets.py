# practice with datasets

with open("data/transactions.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        row # do something with it


# Exercițiu:
# dat fiind fișierul "data/transactions.csv"
# calculați bilanțul curent al fiecărui cont.
#
# creditare = intră bani în cont
# debitare = ies bani din cont


# inițializăm
balances = {}

# procesăm:
# vom folosi account_id drept cheie.
"""
account_id,transaction_type,amount
1,credit,726
2,credit,1317
1,debit,1587
2,debit,267
2,debit,1131
1,credit,1577
"""

balances[account_id] += v
balances[account_id] -= v

# când nu găsim un account_id avem posibilitățile:
# 1) if key in dict
# 2) try / except KeyError
# 3) dict.get(key)
# 4) dict.setdefault()


# rezultat final
import csv

balances = {}
with open("data/transactions.csv") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        acc_id, ttype, amount = row

        acc_id = int(acc_id)
        amount = int(amount)

        if acc_id not in balances:
            balances[acc_id] = 0

        if ttype == 'credit':
            balances[acc_id] += amount
        elif ttype == 'debit':
            balances[acc_id] -= amount
        else:
            # this is a serious bug
            raise Exception("Unkown transaction type: " + ttype)

print(balances)



