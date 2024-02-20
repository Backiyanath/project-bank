class RBI:
    def __init__(self):
        self.total_funds1 = 100000
        self.total_accounts1 = 10000


class SBI(RBI):
    def __init__(self):
        super().__init__()
        self.total_funds2 = 50000
        self.total_accounts2 = 5000


class IndianBank(SBI):
    def __init__(self):
        super().__init__()
        self.total_funds3 = 25000
        self.total_accounts3 = 2500


class CUB(IndianBank):
    def __init__(self):
        super().__init__()
        self.total_funds4 = 12000
        self.total_accounts4 = 1000

    def deposit(self):
        dep = int(input("Enter amount to be deposited: "))
        self.total_funds4 += dep
        print("Amount Deposited:", dep)
        print("Your City Union Bank Account Balance is:", self.total_funds4)
        self.total_funds3 += dep
        print("Indian Bank Account Balance is:", self.total_funds3)
        self.total_funds2 += dep
        print("State Bank Account Balance is:", self.total_funds2)
        self.total_funds1 += dep
        print("Reserve Bank Account Balance is:", self.total_funds1)
        self.withdraw()

    def withdraw(self):
        wd = int(input("Enter your withdrawal amount: "))
        if self.total_funds4 >= wd:
            self.total_funds4 -= wd
            print("Your amount is withdrawn:", wd)
            print("Your City Union Bank Account Balance is:", self.total_funds4)
            self.total_funds3 -= wd
            print("Indian Bank Account Balance is:", self.total_funds3)
            self.total_funds2 -= wd
            print("State Bank Account Balance is:", self.total_funds2)
            self.total_funds1 -= wd
            print("Reserve Bank Account Balance is:", self.total_funds1)
        else:
            print("Insufficient Balance")
            print("Please enter your available balance")
            self.withdraw()

    def open_acc(self):
        open_acc = int(input("Enter the number of accounts to open: "))
        self.total_accounts4 += open_acc
        print("Your Account is Successfully Created in City Union Bank")
        print("Total City Union Bank Accounts:", self.total_accounts4)
        self.total_accounts3 += open_acc
        print("Total Indian Bank Accounts:", self.total_accounts3)
        self.total_accounts2 += open_acc
        print("Total State Bank Accounts:", self.total_accounts2)
        self.total_accounts1 += open_acc
        print("Total Reserve Bank Accounts:", self.total_accounts1)
        self.close_acc()

    def close_acc(self):
        close_acc = int(input("Enter the number of accounts to close: "))
        if self.total_accounts4 >= close_acc:
            self.total_accounts4 -= close_acc
            print("Your Account is successfully closed from City Union Bank")
            print("Total City Union Bank Accounts:", self.total_accounts4)
            self.total_accounts3 -= close_acc
            print("Total Indian Bank Accounts:", self.total_accounts3)
            self.total_accounts2 -= close_acc
            print("Total State Bank Accounts:", self.total_accounts2)
            self.total_accounts1 -= close_acc
            print("Total Reserve Bank Accounts:", self.total_accounts1)
        else:
            print("Sorry, the number of accounts to close exceeds the available accounts in City Union Bank")

    def operate(self):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Open Account\n4. Close Account\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.open_acc()
            elif choice == 4:
                self.close_acc()
            elif choice == 5:
                print("Exiting the system...")
                break
            else:
                print("Invalid choice, please enter a valid option")


if __name__ == "__main__":
    x = CUB()
    x.operate()
