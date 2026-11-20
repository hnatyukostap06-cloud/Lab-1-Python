from decimal import Decimal

import pytest

from bank_accounts.exceptions import InsufficientFundsError, InvalidAmountError
from bank_accounts.models import BankAccount
from bank_accounts.services import (
    calculate_total,
    deposit,
    find_account,
    withdraw,
)


def test_deposit_increases_balance() -> None:
    account = BankAccount("Тест", "UA-1", Decimal("100"))
    assert deposit(account, Decimal("25.50")) == Decimal("125.50")


def test_negative_balance_is_forbidden() -> None:
    account = BankAccount("Тест", "UA-1", Decimal("100"))
    with pytest.raises(InsufficientFundsError):
        withdraw(account, Decimal("101"))
    assert account.balance == Decimal("100")


def test_invalid_amount_is_forbidden() -> None:
    account = BankAccount("Тест", "UA-1", Decimal("100"))
    with pytest.raises(InvalidAmountError):
        deposit(account, Decimal("-1"))


def test_non_finite_amount_is_forbidden() -> None:
    account = BankAccount("Тест", "UA-1", Decimal("100"))
    with pytest.raises(InvalidAmountError):
        deposit(account, Decimal("NaN"))


def test_find_account_and_calculate_total() -> None:
    accounts = [
        BankAccount("Олена", "UA-1001", Decimal("100")),
        BankAccount("Іван", "UA-1002", Decimal("250")),
    ]
    assert find_account(accounts, "ua-1002") is accounts[1]
    assert calculate_total(accounts) == Decimal("350")
