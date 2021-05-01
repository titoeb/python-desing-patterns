# The memento design pattern.
# The memento design pattern is a token/handle representing the system state. It can roll back
# to the state when the token was generated. May or may not directly expose state information.
from __future__ import annotations

# This is our class that we would like to roll back.
class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        return BankAccountSnapshot(self.balance)

    def restore(self, snapshot: BankAccountSnapshot):
        self.balance = snapshot.balance

    def __str__(self):
        return f"Balance = {self.balance}"


# And this is the actual class we will use to roll back the account:
class BankAccountSnapshot:
    def __init__(self, amount: int):
        self.balance = amount


if __name__ == "__main__":
    # This is our original bank account.
    account = BankAccount(100)

    # Let's make two deposits and store the corresponding snapshots
    snapshot_1 = account.deposit(50)
    snapshot_2 = account.deposit(25)

    # This is what our account currently looks like:
    print(account)

    # And because we have the two momentos storing the past state of the bankaccount
    # we can always roll back to it:
    account.restore(snapshot_1)
    print(account)
    account.restore(snapshot_2)
    print(account)