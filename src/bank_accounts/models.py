from dataclasses import dataclass
from decimal import Decimal


@dataclass
class BankAccount:
    customer_name: str
    account_number: str
    balance: Decimal = Decimal("0")

    def __post_init__(self) -> None:
        if not self.customer_name.strip():
            raise ValueError("Ім’я клієнта не може бути порожнім")
        if not self.account_number.strip():
            raise ValueError("Номер рахунку не може бути порожнім")
        if not self.balance.is_finite():
            raise ValueError("Баланс має бути скінченним числом")
        if self.balance < 0:
            raise ValueError("Початковий баланс не може бути від’ємним")
