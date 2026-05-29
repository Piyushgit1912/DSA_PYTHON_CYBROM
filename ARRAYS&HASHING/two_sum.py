class Solution(object):
    def twoSum(self, nums, target):

        d = {}

        for i in range(len(nums)):

            rem = target - nums[i]

            if rem in d:
                return [d[rem], i]

            d[nums[i]] = i

obj=Solution()
print(obj.twoSum([5,7,2,6],7))