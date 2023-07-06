class Invoice:
    def __init__(self, invoice_id, user_id, amount, paid):
        self.invoice_id = invoice_id
        self.user_id = user_id
        self.amount = amount
        self.paid = paid

    def __repr__(self):
        return f"Invoice(invoice_id='{self.invoice_id}', user_id='{self.user_id}', amount='{self.amount}', paid='{self.paid}')"
