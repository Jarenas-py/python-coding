class Solution:
    @staticmethod
    def isPalindrome(x):
        x = str(x)
        reverseList = []
        counter = len(x) - 1

        while counter != -1:
            reverseList.append(x[counter])
            counter -= 1

        reverse = "".join(reverseList)
        return reverse == x

print(Solution.isPalindrome(121))

# Optimized Version (Based by NeetCode)

# The following solution focuses on utilizing math
# instead of converting the input "x" into a string
# in order to determine if input "x" is a Palindrome
# number.

# In this instance, assume that input "x" = 121.

class Solution2:
     @staticmethod
     def twoSum2(x):

        # Step 1: Check if x is negative. If it is, it is not
        # a Palindrome Number so immediately return false.
        if x < 0: return False

        # Step 2: Set up the divider that would serve as 
        # reference later on on the codebase for both checking
        # the topmost value of input x and when removing it 
        # as well for the next number. In the case of x = 121;

        # First Iteration:
        # 121 > 10 * 1. Therefore, 1 * 10 = div = 10

        # Second Iteration:
        # 121 > 10 * 10. Therefore, 10 * 10 = div = 100

        # Third Iteration:
        # 121 < 10 * 100. Therefore, while loop ends. div = 100.
        div = 1
        while x >= 10 * div:
            div *= 10

        # Step 3: Check if current first and last numbers are
        # not equal. If not, return False.
        while x:
            if x // div != x % 10: return False

        # Step 4: Strip away the first and last numbers in 
        # preparation for the next while iteration.

            x = (x % div) // 10
            div = div / 100
        return True

print(Solution2.twoSum2(121))