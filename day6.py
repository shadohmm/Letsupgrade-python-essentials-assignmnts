class bank():
    def __init__(self,ownerName,Balance):
        self.ownerName=ownerName
        self.Balance=Balance
    def deposit(self,money):
        self.Balance+=money
        print('your acc is credited with'+" "+str(money))
    def withdraw(self,money_wanted):
        if money_wanted>self.Balance:
            print("insufficent funds")
        else:
            self.Balance-=money_wanted
            print(str(money_wanted)+" "+"was removed form your acc "+"your balance ammount is:"+" "+str(self.Balance))
    def checq_bal(self):
        print("Balence:"+" "+str(self.Balance))
rajesh=bank("Rajesh",5000)
rakesh=bank("Rakesh",85684)
rajesh.deposit(5244)
jankei=bank("Jankei_Nishad",100000)


rajesh.checq_bal()
rajesh.withdraw(500)
ramkishore=bank("Ram_kishore",50000)
