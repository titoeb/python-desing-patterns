# The memento design pattern.
# The memento design pattern is a token/handle representing the system state. It can roll back
# to the state when the token was generated. May or may not directly expose state information.
from __future__ import annotations

# This is our class that we would like to roll back.
class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.changes = [BankAccountSnapshot(self.balance)]
        self.changes_idx = 0

    def deposit(self, amount: int):
        self.balance += amount
        snapshot = BankAccountSnapshot(self.balance)
        self.changes.append(snapshot)
        self.changes_idx += 1
        return snapshot

    def restore(self, snapshot: BankAccountSnapshot):
        if snapshot:
            self.balance = snapshot.balance
            self.changes.append(snapshot)
            self.changes_idx = len(self.changes) - 1

    def undo(self):
        if self.changes_idx > 0:
            self.changes_idx -= 1
            current_state = self.changes[self.changes_idx]
            self.balance = current_state.balance
            return current_state
        else:
            return None

    def redo(self):
        if self.changes_idx + 1 < len(self.changes):
            self.changes_idx += 1
            current_state = self.changes[self.changes_idx]
            self.balance = current_state.balance
            return current_state
        else:
            return None

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
    account.undo()
    print(f"Undo 1: {account}")
    account.undo()
    print(f"Undo 2: {account}")
    account.redo()
    print(f"Redo: {account}")
    account.redo()
    print(f"Redo 2: {account}")