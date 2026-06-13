import json

class UserAccount:
    def __init__(self, id: int):
        self.id = id
        self.accounts = {}
        self.functions = {"create_account": self.create_account, "deposit": self.deposit, "list_accounts": self.list_accounts}

    def create_account(self, account_id: str, amount: int):
        # business logic, assuming amount is positive, account_id
      if amount <= 0: raise Exception("Negative Amount")
      self.accounts[account_id] = Account(account_id, amount)
      return

    def deposit(self, account_id: str, amount: int):
      self.accounts[account_id].deposit(amount)
      return

    def withdraw(self, account_id: str, amount: int):
      self.accounts[account_id].withdraw(amount)
      return

    def transfer(self, account_id: str, transfer_id: str, amount: int):
      self.accounts[account_id].withdraw(amount)
      self.accounts[transfer_id].deposit(amount)
      return

    def list_accounts(self, **kwargs): 
      for account in self.accounts:
          print(account)

    def batch_dispatch(self, json_input):
        data = json.loads(json_input)
        operations = data["operations"]
        for operation in operations:
            action = operation["action"]
            accountId = operation.get("accountId")
            transferId = operation.get("transferId")
            amount = operation["amount"]
            self.functions[action](accountId, transferId, amount)

class Account:
    balance = 0
    log = []

    def __init__(self, account_id: str, amount: int):
        self.account_id = account_id
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        self.balance -= amount

    def __print__(self):
        print(self.account_id)
        print(self.balance)

# # GUID=0
# Example Input:
#     {
#             "operations" : [
#                 {
#                     "action": "create_account",
#                     "accountId": "A1",
#                     "amount": 100.00
#                     },
#                 {
#                     "action": "create_account",
#                     "accountId": "A2",
#                     "amount": 50.00
#                     },
#                 {
#                     "action": "deposit",
#                     "accountId": "A1",
#                     "amount": 25.00
#                     },
#                 {
#                     "action": "withdraw",
#                     "accountId": "A2",
#                     "amount": 50.00
#                     },
#                 {
#                     "action": "transfer",
#                     "accountId": "A1",
#                     "transferId": "A2",
#                     "amount": 50.00
#                     },
#                 {
#                     "action": "list_accounts"
#                     }
#                 ] 
#             }
#
# Expected Output:
#     {A1:125.00, A2:50.00}
