a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

if(b==0):
    raise ZeroDivisionError("You cannot divide by zero!")
else:
    print(f"The division of {a} by {b} is: {a/b}")


#Another real life example of raising an exception:
def place_order(stock, quantity):
    if quantity > stock:
        raise ValueError("Not enough items in stock")

    return "Order placed"