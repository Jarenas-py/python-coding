class Solution:
    @staticmethod
    def twoSum(nums, target):
        counter = 0
        forCounter = 0
        while True:
            for i in nums:
                if counter == forCounter:
                    forCounter += 1
                    continue

                if nums[counter] + nums[forCounter] == target:
                    return [counter, forCounter]

            if forCounter == len(nums) - 1:
                counter += 1  
                forCounter = 0
                continue

            forCounter += 1 

print(Solution.twoSum([2,7,11,15], 9))