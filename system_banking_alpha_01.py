# Version 001 
# Description:  Creating a Banking System with Python"
# Author: Daniel R Kremes
# Create Date: 10/02/2024 7:13 PM
# Updated Date: 10/03/2024 7:44 PM 
# Todo: deposit, withdraw, stratum
# Todo deposit: 
""" 
    # No need information about:
        """" Number account, Agency, Name User """"
    # Deposit operation: 
    # Should be store in a variable
    # Should be store in a variable stratum
    # Values deposit: only positive not negative
    # Values deposit: only R$ 500.00 by withdraw 
"""
# Todo withdraw:
"""
    # No need information about:
        """" Number account, Agency, Name User """"
    # Withdraw operation: 
    # Should be store in a variable
    # Should be store in a variable stratum
    # Number withdraw day:
        """" 3 by day limit R$ 500,00 """"
    # Withdraw increase balance:
        """" Show message Insufficient funds. """"
    # Values withdraw: only positive not negative
"""


# Variables used to initialize the system -- Mandatory 
balance = 0.0
stratum = 0.0
withdrawals_today = 0
daily_withdrawal_limit = 500


# Message format for menu options
message_menu_options = """
Choose an operation:
1. Deposit
2. Withdraw
3. Check Balance
4. Exit 
"""


while(True):

    # Show value initial balance
    print(f"Balance: {balance}")
    print(f"{message_menu_options}")
    option = str(input("Choose an operation !"))


    if option == '1':
        # Get the value of the amount to deposit
        deposit = float(input("Enter the amount to deposit ? "))
        if deposit > 0:
            balance += deposit
            stratum += balance
            print(f"Deposit successful. New balance: {balance}") 
    

    elif option == '2':
        # Get the value of the amount to withdraw
        amount_withdraw = float(input("Enter the amount to withdraw ? "))
        if amount_withdraw > balance:
            print("Insufficient funds.")
        elif amount_withdraw > 500:
            print("Limit withdraw amount only: R$ 500.00")
            continue
        elif withdrawals_today >= 3:
            print("Daily withdrawal limit exceeded.")
            continue
        elif withdrawals_today >= daily_withdrawal_limit:
              print("You can only withdraw up to R$ 500.00 per transaction.")
        else:
            balance -= amount_withdraw
            withdrawals_today += 1
            print(f"Withdraw successful. New balance: {balance}")
            
        
    elif option == '3':  
        # Get the value of the amount to stratum
        print(f"Balance: {balance}")

    elif option == '4':
        # Exit the system
        break
    else:
        # Invalid option
        print("Invalid option. Please try again.")




