try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program finished.")