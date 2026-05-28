# problem LC217 Contain Duplicates  
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)!=len(set(nums)):
         return True
        else: return False

obj= Solution()
NUMS=[2,3,4,1,2]
print(obj.containsDuplicate(NUMS))