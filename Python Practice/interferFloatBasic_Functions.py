val1 = -5
val2 = 3.14
val3 = -2.335

string1 = "BASIC INT AND FLOAT FUNCTIONS\n"
string2 = f"""The following are the values:

val1 = {val1}
val2 = {val2}
val3 = {val3}

1. We are going to take the absolute value of val1.
2. We are going to round val2 to the nearest whole number.
3. We are going to round val3 to 2 decimal places.\n
"""
string3 = f"""Results:
1. Absolute Value of val1: {abs(val1)}
2. Whole Number Round off of val2: {round(val2)}
3. 2 Decimal Round off of val3: {round(val3, 2)}"""

print(string1)
print(string2)
print(string3)