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
