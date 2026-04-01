val1 = "100"
val2 = 2
val3 = 3.14

newval1 = int(val1)
newval2 = float(val2)
newval3 = int(val3)

string1 = "CASTING\n"
string2 = f"""The following are the values:
val1 = {val1} {type(val1)}
val2 = {val2} {type(val2)}
val3 = {val3} {type(val3)}\n"""
string3 = f"""RESULTS:
1. {newval1} {type(newval1)}
2. {newval2} {type(newval2)}
3. {newval3} {type(newval3)}""" 

print(string1)
print(string2)
print(string3)