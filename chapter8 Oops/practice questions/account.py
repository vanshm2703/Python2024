# create Account with 2 attributes -balance & account no.create methods for debit,credit & printing the balance

class account:
    def __init__(self,bal,acc_num):
        self.balance=bal
        self.account_number=acc_num

    def debit(self,amount):
        self.balance-=amount
        print("RS",amount,"is debited from your account" )
        print("the balance of you account is=" , self.get_balance())
        print("done")

    def credit(self,amount):
        self.balance+=amount
        print("RS",amount,"is credited from your account" )
        print("the balance of you account is=" , self.get_balance())
        print("done")

    def get_balance(self):
        return self.balance


acc1=account(1000,12345)
print(acc1.balance)
print(acc1.account_number)
acc1.credit(1000)
acc1.credit(500)
acc1.debit(100)
acc1.get_balance()