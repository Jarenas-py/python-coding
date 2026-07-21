# The isalnum() method returns a boolean checking
# if a given string has intergers AND characters within it or not.

# The isalpha() strictly checks and returns TRUE
# if a given string only has characters on it.

# isdigit() is the reverse of isalpha()

# islower() returns TRUE if string is all lowercase.

# isspace() returns TRUE if string has any whitespaces.

# isupper() is the opposite of islower() method.



class stringMethods():
    def __init__(self):
        pass

    def isalNum(self):
        a = "hello"
        b = "12hello"
        c = "12312"
        d = "hello_12"

        return f"a Value: {a}, b Value: {b}, c Value: {c}, d Value: {d}\n\n{a.isalnum()} {b.isalnum()}, {c.isalnum()}, {d.isalnum()}\n\n"
    
    def isAlpha(self):
        e = "john"
        f = "john21"

        return f"e Value: {e}, f Value: {f}\n\n{e.isalpha()}, {f.isalpha()}\n\n"

    def isDigit(self):
        g = "asdf1234"
        h = "1234"

        return f"g Value: {g}, h Value: {h}\n\n{g.isdigit()}, {h.isdigit()}\n\n"
    
    def isLower(self) :
        i = "asdfasfd"
        j = "ASDLFKJASDFLKJ"

        return f"i Value: {i}, j Value: {j}\n\n{i.islower()}, {j.islower()}\n\n"
    
    def is_Space(self):
        k = " "
        l = "asdfas asdfdasdf asdfasf"

        return f"k Value: {k}, l Value: {l}\n\n{k.isspace()}, {l.isspace()}\n\n"
    
    def isUpper(self):
        m = "SADFASDF"
        n = "asddfas"

        return f"m Value: {m}, n Value: {n}\n\n{m.isupper()}, {m.isupper()}"
    
firstInstance = stringMethods()
print(firstInstance.isalNum())
print(firstInstance.isAlpha())
print(firstInstance.isDigit())
print(firstInstance.isLower())
print(firstInstance.is_Space())
print(firstInstance.isUpper())