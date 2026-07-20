'''
# option validation
def get_valid_option(option):
    while True:
        option = input(option)
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                return option
            else:
                print("Please select an option between 1 and 4.")
        else:
            print("That's not a number, try again.")


# amount validation
def get_valid_amount(amount):
    while True:
        amount = input(amount)
        if amount.isdigit():
            amount = int(amount)
            return amount
        else:
            print("That's not a number, try again.")
'''
balance = 1000

print("Welcome to Simple Bank!")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

_option = input("Choose an option: ")

if _option.isdigit():
    option = int(_option)
    if option == 1:
        print("Your current balance is: $", balance)
    elif option == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance = balance + amount
        print(f"You have successfully deposited ${amount}. Your new balance is: ${balance}")
    elif option == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print(f"You have successfully withdrawn ${amount}. Your new balance is: ${balance}")
        else:
            print("Insufficient balance! You only have $", balance, "in your account.")
    elif option == 4:
        print("Thank you for using Simple Bank! Goodbye!")
    else:
        print("Invalid choice! Please select an option between 1 and 4.")
else:
    print("Invalid choice! Please select an option between 1 and 4.")
