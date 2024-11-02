class SavingsAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name}, Balance: ${self.balance:.2f}"

    def __lt__(self, other):
        """Compares accounts based on the name."""
        return self.name < other.name

class Bank:
    def __init__(self):
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def __str__(self):
        """Returns a string containing all accounts, sorted by name."""
        sorted_accounts = sorted(self.accounts)
        return "\n".join(str(account) for account in sorted_accounts)

if __name__ == "__main__":
    account1 = SavingsAccount("Charlie", 1500.00)
    account2 = SavingsAccount("Alice", 2000.00)
    account3 = SavingsAccount("Bob", 1000.00)

    bank = Bank()
    bank.addAccount(account1)
    bank.addAccount(account2)
    bank.addAccount(account3)

    print("Accounts in the Bank:")
    print(bank)


