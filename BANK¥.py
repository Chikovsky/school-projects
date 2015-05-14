
# OOP ASSIGNMENT SHELL (Bank Account Manager)

#Your code here for 3 classes
class Accounts(object):
    def __init__(self, Balance):
        self.Balance=Balance
        
    def withdraw(self, amount):
            if  amount > self.Balance:
                print ('You do not have that much in this account.')
            else:
                self.Balance= self.Balance - amount
                print (self.Balance)
    def deposit(self, amount):
            self.Balance=self.Balance + amount
            print (self.Balance)

    def Check_Balance(self):
        print(self.Balance)
        
        
class Savings(Accounts):
    def cal_intrest(self):
        time = int(input('How long has the money been here?(years):'))
        Intrest = self.Balance*0.01
        print('You have earned %s ' %(Intrest))

class Checking(Accounts):
    def withdraw(self, amount):
        if self.Balance < 100:
            print('You must have $100 in this account')
        else:
            print(self.Balance)
            
  
    

print("Welcome tha national bank of Chikosky")
accountType = int(input("What type of account? 1:Savings; 2:Checking?"))
if accountType == 1:
        accountPicked = Savings(1500)
elif accountType == 2:
    accountPicked = Checking(1000)

#Your code here - loop asking the user what they want to do
run = 0
while run ==0:
    Menu = int(input("What would you like to do?: 1.Withdraw 2. Deposit 3. Check Balance 4. Calculate intrest 5. Exit"))
    if Menu == 1:
        amount = int(input('How much would you like to withdraw today?: '))
        accountPicked.withdraw(amount)
    elif Menu == 2:
        amount= int(input('How much would you like to deposit today?:'))
        accountPicked.deposit(amount)
    elif Menu == 3:
       accountPicked.Check_Balance()
    elif Menu == 4:
        accountPicked.cal_intrest()

    else:
        print('Thank you, goodbye.')
        run=1

        
