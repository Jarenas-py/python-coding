class Solution:
    @staticmethod
    def addDigits(num):
        output = 0
        numString = str(num)
        while True:
            for i in numString:
                i = int(i)
                output += i
                print(output)

            if len(str(output)) != 1:
                numString = str(output)
                print(numString)
                continue
            elif len(str(output)) == 1:
                return output

print(Solution.addDigits(38))