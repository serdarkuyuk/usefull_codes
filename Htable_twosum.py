class Solution:
    def twoSum(self, nums, target): 
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
              
son=Solution()
son.twoSum([2,5,6,4], 9)
