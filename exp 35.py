class bank:
    def __init__(self,n,a,t):
        self.acno=a
        self.name=n
        self.typeofac=t
        self.balance=0
    def amt(self):
        print("Account name",self.name)
        print("Acount number",self.acno)
        print("Account Type",self.typeofac)
        print("Balance Amount",self.balance)
    def dep(self,d):
        self.balance=self.balance+d
        return self.balance
    def withd(self,w):
        self.balance=self.balance-w;
        return self.balance
n=input("enter the Account name")
a=int(input("enter the Account number"))
t=input("enter the Account type")

x=bank(n,a,t)
x.amt()
while(True):
    print("\nMenu")
    print("\n1.deposit")
    print("\n2.withdraw")
    c=int(input("enter the choice:"))
    #d=0
    if(c==1):
        d=int(input("enter the acount to deposit :"))
        print("your total Balance Amount is ",x.dep(d))
    elif(c==2):
        w=int(input("enter the amount to be withdrawn: "))
        if(w>d):
            print("insufficient balance")
        else:
            print("your Total Balance Amount is:",x.withd(w))
    else:
        print("enter a valid choice:")