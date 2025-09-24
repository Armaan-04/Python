class BankAccount:
    def __init__(self , account_number , balance):
        self.account_number = account_number
        self.__balance = balance  #The " __" changes balance to a private variable from public variable
        
    def deposit(self , amount):
        self.__balance += amount
        print(f'Deposited {amount} , new balance {self.__balance}')
        
    def get_balance(self):
        return self.__balance #controlled access
    
account = BankAccount('12345' , 5000)

account.deposit(2000)
print(account.get_balance())

#print(account.__balance) -> this line will give an error since __balance is a pvt variable


        