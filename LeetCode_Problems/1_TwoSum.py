class Solution:
    @staticmethod
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] + nums[j] == target:
                    return [i, j]

# Optimized Version (Based on Neetcode)

# The following optimized version utilizes
# python hashmaps (dictionary) and utilizing difference
# at each iteration in order to find the addens, 
# updating the hashmap, and finally finding the addens
# of "target." This methodology is a "one pass" method.
# Meaning it can find the required indices at one loop.

# Given Example: ([2,1,5,3], 4)

class Solution2:
    @staticmethod
    def twoSum2(nums, target):
        # Step 1: Create an empty hashmap.
        prevMap = {}

        for i, n in enumerate(nums):

        # Step 2: Subtract the target sum to the value
        # iteration.
            diff = target - n

        # Step 3: If the difference (the other addens)
        # is present in the hashmap, return the dictionary
        # value of diff from the hashmap (dictionary) prevMap
        # and the value of i which serves as the index of the 
        # current iteration adden.
            if diff in prevMap:
                return [prevMap[diff], i]

        # Step 4: If that is not the case, store the current 
        # key (value or adden) as well as its index in the 
        # given list which is nums (i).
            prevMap[n] = i
        return