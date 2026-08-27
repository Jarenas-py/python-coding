class Solution:
    @staticmethod
    def containsDuplicate(nums):
        return len(nums) != len(set(nums))