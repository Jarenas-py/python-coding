def calculator (tip, totalCost):
    tip= (tipPercent/100)*price
    totalCost= tip + price
    return tip, totalCost

print("\nTIP CALCULATOR")
print("Enter the price of the meal and the tip percentage.")
price= float(input("\nEnter the price: "))
tipPercent= float(input("Enter the Tip Percentage: "))
if (tipPercent > 100 or tipPercent < 0):
    print("Error: Enter a valid tip percentage.")
    exit()

tip, totalCost= calculator(price, tipPercent)

print(f"\nThe tip is {tip:.2f}%")
print(f"The total cost would be {totalCost:.2f} php")