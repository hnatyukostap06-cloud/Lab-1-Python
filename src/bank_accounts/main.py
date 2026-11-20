from decimal import Decimal, InvalidOperation

from bank_accounts.exceptions import BankAccountError
from bank_accounts.models import BankAccount
from bank_accounts.services import (
    calculate_total,
    deposit,
    find_account,
    get_balance,
    sort_accounts_by_balance,
    withdraw,
)


def create_demo_accounts() -> list[BankAccount]:
    return [
        BankAccount("Олена Коваленко", "UA-1001", Decimal("12500.50")),
        BankAccount("Іван Петренко", "UA-1002", Decimal("4800")),
        BankAccount("Марія Шевченко", "UA-1003", Decimal("15320.75")),
    ]


def format_money(amount: Decimal) -> str:
    return f"{amount:.2f} грн"


def print_accounts(accounts: list[BankAccount]) -> None:
    print("\nСписок банківських рахунків:")
    print(f"{'Клієнт':20} {'Номер':12} {'Баланс':>15}")
    print("-" * 47)
    for account in accounts:
        print(
            f"{account.customer_name:20} "
            f"{account.account_number:12} "
            f"{format_money(account.balance):>15}"
        )


def read_amount(prompt: str) -> Decimal | None:
    try:
        amount = Decimal(input(prompt).strip().replace(",", "."))
        if not amount.is_finite():
            print("Помилка: введіть коректне числове значення.")
            return None
    except InvalidOperation:
        print("Помилка: введіть коректне числове значення.")
        return None
    return amount


def print_menu() -> None:
    print("\n1. Показати всі рахунки")
    print("2. Поповнити рахунок")
    print("3. Зняти кошти")
    print("4. Перевірити баланс")
    print("5. Знайти рахунок")
    print("6. Загальна сума коштів")
    print("7. Рахунки за спаданням балансу")
    print("8. Вийти")


def run_menu(accounts: list[BankAccount]) -> None:
    while True:
        print_menu()
        command = input("Оберіть пункт меню: ").strip()

        if command == "1":
            print_accounts(accounts)
        elif command in {"2", "3", "4", "5"}:
            account_number = input("Введіть номер рахунку: ").strip()
            account = find_account(accounts, account_number)
            if account is None:
                print("Рахунок не знайдено.")
                continue

            if command == "2":
                amount = read_amount("Сума поповнення: ")
                if amount is None:
                    continue
                try:
                    new_balance = deposit(account, amount)
                    print(f"Поповнення виконано. Новий баланс: {format_money(new_balance)}")
                except BankAccountError as error:
                    print(f"Помилка: {error}")
            elif command == "3":
                amount = read_amount("Сума зняття: ")
                if amount is None:
                    continue
                try:
                    new_balance = withdraw(account, amount)
                    print(f"Зняття виконано. Новий баланс: {format_money(new_balance)}")
                except BankAccountError as error:
                    print(f"Помилка: {error}")
            elif command == "4":
                print(f"Баланс рахунку: {format_money(get_balance(account))}")
            else:
                print(
                    f"Знайдено: {account.customer_name}, "
                    f"{account.account_number}, баланс {format_money(account.balance)}"
                )
        elif command == "6":
            print(f"Загальна сума коштів: {format_money(calculate_total(accounts))}")
        elif command == "7":
            print_accounts(sort_accounts_by_balance(accounts))
        elif command == "8":
            print("До побачення!")
            break
        else:
            print("Невідомий пункт меню.")


def main() -> None:
    run_menu(create_demo_accounts())


if __name__ == "__main__":
    main()
