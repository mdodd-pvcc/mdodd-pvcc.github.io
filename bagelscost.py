# Name: Marisa-Dodd
# Prog Purpose: This program creates a sales receipt for Brownsville Bagels
# Price for one bagel: $2.25
# Price for cream cheese: $1.25
# Sales tax rate: 6%

import datetime

# Define global variables
SALES_TAX_RATE = 0.06
PR_BAGEL = 2.25
PR_CREAMCH = 1.25
num_bagels = 0
num_creamch = 0
cost_bagels = 0
cost_creamch = 0
subtotal = 0
sales_tax = 0
total = 0

# Define program functions
def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data():
    global num_bagels, num_creamch
    num_bagels = int(input("Number of bagels: "))
    num_creamch = int(input("Number of cream cheese: "))

def perform_calculations():
    global cost_bagels, cost_creamch, subtotal, sales_tax, total
    cost_bagels = num_bagels * PR_BAGEL
    cost_creamch = num_creamch * PR_CREAMCH
    subtotal = cost_bagels + cost_creamch
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('--------------------------------')
    print('BROWNSVILLE BAGEL COMPANY')
    print('Fresh-baked bagels every day!')
    print('--------------------------------')
    print(f'Bagels       $ {cost_bagels:8,.2f}')
    print(f'Cream Cheese $ {cost_creamch:.2f}')
    print('--------------------------------')
    print(f'Subtotal     $ {subtotal:.2f}')
    print(f'Sales Tax    $ {sales_tax:.2f}')
    print(f'Total        $ {total:.2f}')
    print('--------------------------------')
    print(datetime.datetime.now())

# Call the main program to execute
main()
