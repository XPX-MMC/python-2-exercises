from pprint import pprint
from ex8 import CarCollector
from ex9 import Fighter, Dwarf, Knight
from ex10 import Invoice

def sort_people(people, weight, direction):
     pass #TODO:

people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
sort_people(people_list, 'weight', 'desc')
# print(people_list)


def ex8():
    pprint(CarCollector.get_data())

# ex8()
# EXPECTED OUTPUT:
# [{'id': 1, 'make': 'Ford', 'price': 10000},
#  {'id': 2, 'make': 'Mazda', 'price': 20000},
#  {'id': 3, 'make': 'Chevy', 'price': 30000}]

def ex9():
    f = Fighter(100, 10)
    d = Dwarf(85, 15)
    k = Knight(125, 8)


    print(k)
    print(f)
    print(d)

    k.fight(f)
    f.fight(d)
    d.fight(k)

    print(f)
    print(d)
    print(k)

# ex9()

# EXPECTED OUTPUT:
# Fighter: 18 hit points.
# Drawf: 15 hit points.
# Fighter: <random> hit points.
# Drawf: <random> hit points.


def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]

    invoices_list = []

    for item in data:
        invoice_id, user_id, amount, paid = item.split(", ")

        invoices_list.append(
            Invoice(invoice_id, user_id, amount, paid)
        )

    print(invoices_list)

ex10()
# EXPECTED OUTPUT:
# [Invoice(invoice_id='1', user_id='2322', amount='10.00', paid='False'), Invoice(invoice_id='2', user_id='5435', amount='60.30', paid='True'), Invoice(invoice_id='3', user_id='3433', amount='15.63', paid='False'), Invoice(invoice_id='4', user_id='8439', amount='12.77', paid='False'), Invoice(invoice_id='5', user_id='3424', amount='11.34', paid='False')]

