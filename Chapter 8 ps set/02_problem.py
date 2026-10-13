#program to convert temperature from Fahrenheit to Celsius using funciton:
def f_to_c():
    return (f - 32) * 5 / 9

f=int(input("Enter the temperature in Fahrenheit: "))
print(f"The temperature in Celsius is: {f_to_c():.2f}") 