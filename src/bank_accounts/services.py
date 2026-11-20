from decimal import Decimal

from bank_accounts.exceptions import InsufficientFundsError, InvalidAmountError
from bank_accounts.models import BankAccount


def validate_amount(amount: Decimal) -> None:
    if not amount.is_finite():
        raise InvalidAmountError("Сума має бути скінченним числом")
    if amount <= 0:
        raise InvalidAmountError("Сума повинна бути додатною")


def deposit(account: BankAccount, amount: Decimal) -> Decimal:
    validate_amount(amount)
    account.balance += amount
    return account.balance


def withdraw(account: BankAccount, amount: Decimal) -> Decimal:
    validate_amount(amount)
    if amount > account.balance:
        raise InsufficientFundsError("Недостатньо коштів на рахунку")
    account.balance -= amount
    return account.balance


def get_balance(account: BankAccount) -> Decimal:
    return account.balance


def find_account(
    accounts: list[BankAccount],
    account_number: str,
) -> BankAccount | None:
    normalized_number = account_number.strip()
    for account in accounts:
        if account.account_number.lower() == normalized_number.lower():
            return account
    return None


def calculate_total(accounts: list[BankAccount]) -> Decimal:
    return sum((account.balance for account in accounts), Decimal("0"))


def sort_accounts_by_balance(
    accounts: list[BankAccount],
    descending: bool = True,
) -> list[BankAccount]:
    return sorted(
        accounts,
        key=lambda account: account.balance,
        reverse=descending,
    )
