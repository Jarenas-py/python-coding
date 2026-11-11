class Solution:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def two_check(self):
        left = 0
        right = len(self.arr) - 1

        while left < right:
            curr = self.arr[left] + self.arr[right]
            print(self.arr[left])
            print(self.arr[right])
            print(curr)
            if curr == self.target: return [left + 1, right + 1]

            if curr > self.target:
                right -= 1
            else:
                left += 1

instance1 = Solution([2, 7 ,11 ,15], 9)
print(instance1.two_check())