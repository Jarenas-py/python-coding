class Solution:
    @staticmethod
    def majorityElement(nums):
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        for j in hashMap:
            if max(hashMap.values()) == hashMap[j]:
                return j

# The following codebase reflects the optimized logic
# with regards to the problem. There is no need for 
# an optimized version by NeetCode.