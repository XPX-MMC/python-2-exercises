from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Invoice:
    invoice_id: int
    user_id: int
    amount: float
    paid: False
