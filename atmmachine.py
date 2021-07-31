# Front-End File

from atmsim import User
import time


# This function shows the menu screen.
# It runs until a valid choice is made
def show_menu():
    while True:
        print("WELCOME TO THE ATM")
        print("_______________")
        print("1. Add A New Account")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Check Balance")
        print("5. Exit ATM")
        response = input("Choice: ")
        print()

        if response == "1":
            add_user()
        elif response == "2":
            deposit_funds()
        elif response == "3":
            withdraw_funds()
        elif response == "4":
            check_balance()
        elif response == "5":
            break
        else:
            print("Invalid Choice")
            print()


# This function allows new bank users to be added
# Function asks for a name and surname and then generates a pin
def add_user():
    name = input("Name: ")
    surname = input("Surname: ")
    pin = User.get_pin()
    print("This is your pin:", pin)
    print("Please memorise it...")
    User(name, surname, pin)
    print()
    time.sleep(2)


# Function to deposit funds
# User has to enter his pin to access his account - This has to be done for every functionality of the program
# Alternatively the program could have allowed the user to access his account with his pin and then be able to access
# every program functionality
# For some reason, the chosen way seemed more realistic even though it is more inconvenient for the end user
def deposit_funds():
    user_pin = input("Please enter your pin: ")
    u = check_pin(user_pin)

    print("This is your current balance:", "€{:,.2f}".format(u.balance))
    deposit = input("How much money would you like to deposit: €")
    u.balance = float(u.balance) + float(deposit)
    print("Please enter", "€{:,.2f}".format(float(deposit)), "into the machine...")
    time.sleep(2)
    print("Your new balance is now:", "€{:,.2f}".format(u.balance))
    time.sleep(2)
    print()


# Function to withdraw funds
# Again user has to enter pin to access account
# Only allowed to withdraw funds if the funds are available
# Worth noting this is a futuristic ATM machine that accepts coins
def withdraw_funds():
    user_pin = input("Please enter your pin: ")
    u = check_pin(user_pin)

    print("This is your current balance:", "€{:,.2f}".format(u.balance))

    while True:
        print()
        withdraw = input("How much money would you like to withdraw: €")
        if float(withdraw) > float(u.balance):
            print("You have insufficient money in your account")
            print("Please decrease the amount of money you would like to withdraw")
        else:
            u.balance = float(u.balance) - float(withdraw)
            print("Please take your", "€{:,.2f}".format(float(withdraw)), "from the machine...")
            time.sleep(2)
            print("Your new balance is now:", "€{:,.2f}".format(u.balance))
            time.sleep(2)
            print()
            break


# Function for the user check the bank balance
def check_balance():
    user_pin = input("Please enter your pin: ")
    u = check_pin(user_pin)

    print("This is your current balance:", "€{:,.2f}".format(u.balance))
    time.sleep(4)


# Function to check whether the entered pin is valid
# user is asked to re-enter pin if invalid
def check_pin(user_pin):
    while True:
        u = User.get_by_pin(user_pin)
        if not User.get_by_pin(user_pin):
            print("Invalid Pin")
            print()
            user_pin = input("Please enter your pin: ")
        else:
            break
    print("Welcome", u.name, u.surname)
    return u


show_menu()
