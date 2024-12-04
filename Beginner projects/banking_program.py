""" WELCOME TO THE BANKING PROGRAM"""

def show_balance(balance):
    print("***********************************")
    print(f"Your balance: ${balance:.2f}")
    print("***********************************")
def deposit():
    print("***********************************")
    amount = float(input("Enter an amount to be deposited:"))
    print("***********************************")

    if amount < 0:
        print("***********************************")
        print("Allowed only positive number of amount: ")
        print("***********************************")
        return 0
    else:
        return amount
def withdrawn(balance):
    print("***********************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("***********************************")
    if amount > balance:
        print("***********************************")
        print("Insufficient funds")
        print("***********************************")
        return 0
    elif amount <0:
        print("***********************************")
        print("Amount must be greater then 0")
        print("***********************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("***********************************")
        print("  Welcome to the banking program  ")
        print("1.Show balance \n2.Deposit \n3.Withdraw \n4.Exit ")
        print("***********************************")
        user_choice = input("Enter your choice(1,2,3,4): ")

        if user_choice == '1':
            show_balance(balance)
        elif user_choice == '2':
            balance += deposit()
            show_balance(balance)
        elif user_choice == '3':
            balance -= withdrawn(balance)
        elif user_choice == '4':
            is_running = False
        else:
            print("***********************************")
            print("Please, enter the number by the list below: ")
            print("***********************************")
    print("***********************************")
    print("Your request is up. Thank you for using our services!")
    print("***********************************")

if __name__ == '__main__':
    main()