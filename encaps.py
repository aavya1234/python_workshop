class bankaccount:
    def __init__(self,account_number,balance):
        self._account_number=account_number
        self.__balance=balance
    def get_balance(self):
        return self.get_balance
account=bankaccount("12345",1000)
print(account._account_number)
print(account.get_balance)