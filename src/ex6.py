class TaxMan:

    def __init__(self, items, tax):
        self._tax = float(tax[0:2]) / 100
        self._total = 0.00
        self.items = items

    def calc_total(self):
        self._total = sum(list(map(lambda i: i["price"], self.items)))
        taxes = self._total * self._tax
        self._total += taxes

    def get_total(self):
        return self._total


def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())

ex6()
