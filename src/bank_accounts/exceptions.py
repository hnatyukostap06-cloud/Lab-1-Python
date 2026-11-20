class BankAccountError(Exception):
    """Base exception for bank account operations."""


class InsufficientFundsError(BankAccountError):
    """Raised when an account does not have enough funds."""


class InvalidAmountError(BankAccountError):
    """Raised when an amount is not positive."""
