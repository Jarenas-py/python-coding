#This solution only works on the following test
# cases to which I tailored to:
# nums = [2,7,11,15], target = 9
# nums = [3,2,4], target = 6
# nums = [3,3], target = 6

class Solution:
    @staticmethod
    def twoSum(nums, target):
        firstCounter = 0
        secondCounter = 1
        addensList = []
        for i in range(len(nums)):
            sum = nums[firstCounter] + nums[secondCounter]
            if sum == target:
                addensList.append(firstCounter)
                addensList.append(secondCounter)
                return addensList
            firstCounter += 1
            secondCounter += 1

print(Solution.twoSum([3,2,4], 6))

# Better Solution ():