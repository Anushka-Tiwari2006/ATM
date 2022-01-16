class atm(object):
    def __init__(self,nameOfUser,bankName,currentBalance):
        self.nameOfuser = nameOfUser
        self.bankName = bankName
        self.currentbalance = currentBalance
        
    def CashWithdrawl(self):
        print("The cash has been withdrawl succesfully")
        
    def CashDeposit(self):
        print("The cash has been deposited succesfully")
        
    def MaximamWithdrawl(self):
        print("Maximum amount you can withdraw is INR 50,000/- ")
        
atm1 = atm("Anushka","Axis Bank",1000000)
atm2 = atm("Rashi","SBI Bank",75000)

print(atm1.MaximamWithdrawl())
print(atm2.CashDeposit())
print(atm1.CashWithdrawl())

