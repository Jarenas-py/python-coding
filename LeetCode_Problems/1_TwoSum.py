class Solution:
    @staticmethod
    def twoSum(nums, target):
        counter = 0
        forCounter = 0
        for i in nums:
            if counter == forCounter:
                forCounter += 1
                continue

            if nums[counter] + nums[forCounter] == target:
                return [counter, forCounter]

            counter += 1
            continue

print(Solution.twoSum([3,2, 4], 6))