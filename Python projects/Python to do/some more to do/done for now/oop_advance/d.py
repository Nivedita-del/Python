class Bank():
    def __init__(self, balance):
        self.balance = balance

    @staticmethod
    def find_interest(loan_money, interest_rate):
        return loan_money * (1 + interest_rate)

    @classmethod
    def find_interest_classmethod(cls, loan_money):
        return loan_money * 1.4

    def find_interest_instancemethod(self, loan_money):
        if self.balance <= 100:
            return loan_money * 1.2
        else:
            return loan_money * 1.5


class ATM(Bank):
    def __init__(self, balance):
        super().__init__(balance)

    @staticmethod
    def find_interest(loan_money):
        return loan_money * 1.3


atm = ATM(1000)
print('Using staticmethod ->', atm.find_interest(atm.balance))
print('Using classmethod from the parent class ->', Bank.find_interest_classmethod(atm.balance))
print('Using classmethod from the inherited subclass ->', ATM.find_interest_classmethod(atm.balance))
print('Using a regular instance method ->', atm.find_interest_instancemethod(atm.balance))