# The command design pattern.
# A command is an object that represents an instruction to perform a particual action. Contains all the
# information necessary for the action to be taken.
from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: int) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")

    def __str__(self):
        return f"Balance: {self.balance}"


# So good so far. We have nicely working bank account. But we also want
# to have some safety, and as requirement all operations on bank accounts
# need to be stored. How to do it?


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 1
        WITHDRAW = 2

    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.withdraw(self.amount)

    def undo(self):
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    bank_account = BankAccount(balance=0)
    command = BankAccountCommand(bank_account, BankAccountCommand.Action.DEPOSIT, 100)
    command.invoke()
    print(bank_account)

    command.undo()
    print(bank_account)

# So far, so nice. We have a dedicted command class which we can use to do our defined
# operations (Deposit / Withdraw) on our bank account. Also, we can even undo them now.
# But doing the withdraw operation as inverse of the deposit operation is not 100% correct.
# Let's see how it can go wrong:
if __name__ == "__main__":
    illegal_command = BankAccountCommand(
        bank_account, BankAccountCommand.Action.WITHDRAW, 10000
    )
    print(bank_account)
    illegal_command.invoke()
    print(bank_account)
    illegal_command.undo()
    print(bank_account)

# UUH! We just made 10000 euro ;)
# Let's fix it.
class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: int) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited {amount}, new balance: {self.balance}")
        return True

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")
            return True
        else:
            return False

    def __str__(self):
        return f"Balance: {self.balance}"


# So good so far. We have nicely working bank account. But we also want
# to have some safety, and as requirement all operations on bank accounts
# need to be stored. How to do it?


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 1
        WITHDRAW = 2

    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.success = self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if self.success:
            if self.action == self.Action.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.action == self.Action.WITHDRAW:
                self.account.deposit(self.amount)


if __name__ == "__main__":
    print("After fixing undoing impossible withdraws:")
    bank_account = BankAccount(balance=0)

    illegal_command = BankAccountCommand(
        bank_account, BankAccountCommand.Action.WITHDRAW, 10000
    )
    print(bank_account)
    illegal_command.invoke()
    print(bank_account)
    illegal_command.undo()
    print(bank_account)
