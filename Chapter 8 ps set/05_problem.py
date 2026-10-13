#program to convert length from inches to centimeters using function:
def inches_to_centi():
    centi = inches * 2.54
    return centi
    
inches = float(input("Enter the length in inches: "))
print(f"The length in centimeters is: {inches_to_centi():.2f}")