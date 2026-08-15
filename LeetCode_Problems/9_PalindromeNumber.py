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


print(Solution.isPalindrome(1234512))