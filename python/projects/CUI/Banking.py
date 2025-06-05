#Banking program

amount = 0.0

def create_account():
    print("Account created successfully!")

def deposit_money():
    amount1 = float(input("Enter amount to deposit: "))
    print(f"Deposited ${amount1:.2f} successfully!")
    global amount
    amount += amount1 

def withdraw_money():
    amount2 = float(input("Enter amount to withdraw: "))
    print(f"Withdrew ${amount2:.2f} successfully!")
    global amount
    if amount2 <= amount:
        amount -= amount2
    else:
        print("Insufficient funds for withdrawal.")

def check_balance():
    global amount
    balance = amount  # Placeholder for balance
    print(f"Your current balance is: ${balance:.2f}")

def main():
    print("Welcome to the Banking Program")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    while True:
        choice = input("Please enter your choice (1-5): ")
        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using the Banking Program!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

