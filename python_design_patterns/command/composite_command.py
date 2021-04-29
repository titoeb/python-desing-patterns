# The command design pattern.
# A command is an object that represents an instruction to perform a particual action. Contains all the
# information necessary for the action to be taken.
from __future__ import annotations
from typing import List
from abc import ABC
import unittest
from enum import Enum


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


class Command(ABC):
    def __init__(self) -> None:
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 1
        WITHDRAW = 2

    def __init__(self, account, action, amount):
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account

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


class CompositeBankAccountCommand(Command, list):
    def __init__(self, commands: List[BankAccountCommand] = []) -> None:
        super().__init__()
        for command in commands:
            self.append(command)

    def invoke(self):
        for command in self:
            command.invoke()

    def undo(self):
        for command in reversed(self):
            command.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(
        self, from_account: BankAccount, to_account: BankAccount, amount
    ) -> None:
        super().__init__(
            commands=[
                BankAccountCommand(
                    account=from_account,
                    action=BankAccountCommand.Action.WITHDRAW,
                    amount=amount,
                ),
                BankAccountCommand(
                    to_account, BankAccountCommand.Action.DEPOSIT, amount
                ),
            ]
        )

    def invoke(self):
        ok = True
        for command in self:
            if ok:
                ok = command.invoke()
            else:
                command.success = False
            self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        bank_account = BankAccount(100)
        deposit1 = BankAccountCommand(
            bank_account, BankAccountCommand.Action.DEPOSIT, 100
        )
        deposit2 = BankAccountCommand(
            bank_account, BankAccountCommand.Action.DEPOSIT, 50
        )
        deposit3 = BankAccountCommand(
            bank_account, BankAccountCommand.Action.WITHDRAW, 75
        )

        composite_deposit = CompositeBankAccountCommand([deposit1, deposit2, deposit3])
        composite_deposit.invoke()
        assert bank_account.balance == 175
        composite_deposit.undo()
        assert bank_account.balance == 100

    # def test_transfer_fail(self):
    #     bank_account_1 = BankAccount(100)
    #     bank_account_2 = BankAccount(0)

    #     withdraw = BankAccountCommand(
    #         bank_account_1, BankAccountCommand.Action.WITHDRAW, 10000
    #     )
    #     deposit = BankAccountCommand(
    #         bank_account_2, BankAccountCommand.Action.DEPOSIT, 10000
    #     )

    #     transfer = CompositeBankAccountCommand([withdraw, deposit])
    #     transfer.invoke()
    #     assert bank_account_1.balance + bank_account_2.balance == 100

    #     transfer.undo()
    #     assert bank_account_1.balance + bank_account_2.balance == 100
    def test_transfer_suceed(self):
        bank_account_1 = BankAccount(100)
        bank_account_2 = BankAccount(0)
        transfer = MoneyTransferCommand(
            from_account=bank_account_1, to_account=bank_account_2, amount=1000
        )
        transfer.invoke()
        assert bank_account_1.balance + bank_account_2.balance == 100

        transfer.undo()
        assert bank_account_1.balance + bank_account_2.balance == 100

    def test_transfer_suceed(self):
        bank_account_1 = BankAccount(100)
        bank_account_2 = BankAccount(0)
        transfer = MoneyTransferCommand(
            from_account=bank_account_1, to_account=bank_account_2, amount=100
        )
        transfer.invoke()
        assert bank_account_1.balance + bank_account_2.balance == 100
        assert bank_account_1.balance == 0
        assert bank_account_2.balance == 100

        transfer.undo()
        assert bank_account_1.balance + bank_account_2.balance == 100
        assert bank_account_1.balance == 100
        assert bank_account_2.balance == 0


if __name__ == "__main__":
    unittest.main()
