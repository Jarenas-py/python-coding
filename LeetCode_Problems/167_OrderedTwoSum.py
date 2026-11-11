class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target: return [left + 1, right + 1]

            if curr > target:
                right -= 1
            else:
                left += 1