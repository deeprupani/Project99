class ATM():
    def __init__(self, pin, cardNo):
        self.pin = pin
        self.cardNo = cardNo
        self.balance = 1000

    def checkBalance(self):
        print(self.balance)

    def withdrawal(self, amount):
        if(self.balance<amount):
            print(f"Your balance was {self.balance} You can only withdraw {self.balance}")
        else:
            self.balance = self.balance - amount
            print(self.balance)


    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)


def main():
    cardNo = input("Enter your Card No ")
    pinNo = input("Enter your Pin No ")
    myAccount = ATM(pinNo, cardNo)

    while (True):
        print("Type 1 for Balance,Type 2 for Withdrawal,Type 3 for Deposit,Type 4 to exit")
        choice = int(input("Enter your choice No "))
        if choice == 1:
            myAccount.checkBalance()
        elif choice == 2:
            amount = int(input("Enter the Amount "))
            myAccount.withdrawal(amount)
        elif choice == 3:
            amount = int(input("Enter the Amount "))
            myAccount.deposit(amount)
        elif choice == 4:
            print("Thanks for using the ATM")
            exit()
        else:
            print("Enter a Valid No ")
            choice = int(input("Enter your choice No "))


main()
