var1 = 5.6
var2 = -2

castVar1 = int(var1)
castVar2 = abs(var2)

equalTo = castVar1 == castVar2
notEqualTo = castVar1 != castVar2
greaterThan = castVar1 > castVar2
lessThan = castVar1 < castVar2
greaterThanOrEqualTo = castVar1 >= castVar2
lessThanOrEqualTo = castVar1 <= castVar2

string1 = "COMPARISON OPERATORS IN PYTHON\n"
string2 = f"""VALUES
1. var1 {var1} casted into int {castVar1}
2. var2 {var2} casted into absolute value {castVar2}\n"""
string3 = f"""RESULTS:
1. 5 = 2 {equalTo}
2. 5 != 2 {notEqualTo}
3. 5 > 2 {greaterThan}
4. 5 < 2 {lessThan}
5. 5 >= 2 {greaterThanOrEqualTo}
6. 5 <= 2 {lessThanOrEqualTo}"""

print(string1)
print(string2)
print(string3)