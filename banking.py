def show_balance(balance):
    print("--------------------")
    print(f"Your Balance is ${balance:.2f}")
    print("--------------------")

def deposit():
    print("--------------------")
    amount = float(input("Enter an amount to be deposited: "))
    print("--------------------")

    if amount < 0:
        print("--------------------")
        print("That's not a valid amount")
        print("--------------------")
        return 0
    else:
        return amount

def withdraw(balance):
    print("--------------------")
    amount = float(input("Enter an amount to be withdraw: "))
    print("--------------------")

    if amount > balance:
        print("--------------------")
        print("Insufficient Funds")
        print("--------------------")
        return 0
    elif amount < 0:
        print("--------------------")
        print("Amount must be greater than 0")
        print("--------------------")
        return 0 
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("--------------------")
        print("Welcome to the Bank")
        print("--------------------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("--------------------")

        choice = input("Enter your choice : ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("--------------------")
            print("That is not a valid choice")
            print("--------------------")

    print("--------------------")
    print("Thankyou and have a nice day!")
    print("--------------------")

if __name__ == '__main__':
    main()