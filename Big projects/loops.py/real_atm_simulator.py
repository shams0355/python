print("================================")
print("      \033[1m WELCOME TO MY ATM\033[0m")
print("================================")

balance = 50000
correct_pin = 1234
attempts = 0

pin = int(input("Enter your PIN: "))

while not(pin== correct_pin )and attempts < 3:
    print("Wrong PIN!")
    attempts = attempts + 1

    if attempts < 3:
        pin = int(input("Enter your PIN again: "))
    else:
        print("Your account is blocked.")

if pin == correct_pin:

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your current balance is:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance = balance - amount
                print("Please collect your cash.")
                print("Remaining balance:", balance)

            else:
                print("Insufficient balance.")

        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))

            if amount > 0:
                balance = balance + amount
                print("Amount deposited successfully.")
                print("New balance:", balance)
            else:
                print("Invalid amount.")

        elif choice == 4:
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice.")

else:
    print("Access denied.")