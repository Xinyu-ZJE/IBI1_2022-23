def whether_buy_house(value, salary):
    if value > 5*salary:
        return "It's not recommended to buy this house."
    else:
        return "You can buy this house."
# The following are examples
# If salary is 35000, and the value of the house is 180000
x=whether_buy_house(180000,35000)
print(x)
# The output is 'It's not recommended to buy this house.'
y=whether_buy_house(180000,36000)
print(y)
# The output is 'You can buy this house.'
