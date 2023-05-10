class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        plm = set()
        indices = dict()
        for indice, num in enumerate(nums):
            if target - num in plm:
                return [indice, indices[target-num]]
            
            plm.add(num)
            indices[num] = indice

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))