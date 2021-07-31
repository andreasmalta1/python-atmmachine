# Create an ATM simulation program. The program must allow the user to:
# Check their balance.
# Withdraw funds.
# Deposit funds.
# The program must not allow users to withdraw more funds than their account holds.
# For extra credit, create multiple account instances, each with a PIN required prior to accessing the account.

# Back-End File

import random


# The User class wil store all the different users who have a bank account
# The User class will have store the user's name, surname, pin and balance
# The balance is set at €0.00 when setting up the account
# The USER_LIST saves all the instances in the User class
class User:
    USER_LIST = []

    def __init__(self, name: str, surname: str, pin):
        self.name = name
        self.surname = surname
        self.__pin = pin
        self.balance = 0.00
        User.USER_LIST.append(self)

    # The get_by_pin method allows the program to search for the users from the pin entered in the CLI
    @staticmethod
    def get_by_pin(user_pin):
        for u in User.USER_LIST:
            if u.pin == user_pin:
                return u

    # The get_pin method is called from the atmmachine file and generates a random 4 digit pin
    # To check if the pin is unique, all pins including the new one are added to a list
    # The set function is used to recreate the list using only duplicate values
    # If there are duplicate values, the last pin is removed and re-generated
    # Once a pin is accepted it is stored in the user's account
    # This method was checked that it works successfully by changing the range of pins to an upper limit of 5.
    @staticmethod
    def get_pin():
        pin_check_list = []
        for u in User.USER_LIST:
            pin_check_list.append(u.pin)
        while True:
            pin_num = (format(random.randint(0000, 9999), '04d'))
            print(pin_num)
            pin_check_list.append(pin_num)
            if len(pin_check_list) > len(set(pin_check_list)):
                pin_check_list.pop()
            else:
                break
        return pin_num

    # Function to be able to access the pin from the atmmachine file
    @property
    def pin(self):
        return self.__pin
