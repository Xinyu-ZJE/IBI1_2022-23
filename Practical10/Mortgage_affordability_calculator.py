def whether_buy_house(value, salary):
    if value > 5*salary:
        print("It's not recommended to buy this house.")
    else:
        print("You can buy this house")
# The following are examples
# If salary is 35000, and the value of the house is 180000
whether_buy_house(180000,35000)
# The output is 'It's not recommended to buy this house.'
whether_buy_house(180000,36000)
# The output is 'You can buy this house.'
