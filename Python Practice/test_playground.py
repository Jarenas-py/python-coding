def F(n):
    if n <= 1:
        return n

    oneBack = F(n-1)
    twoBack = F(n-2)
    return oneBack + twoBack

print(F(2))