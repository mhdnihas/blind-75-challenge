class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        
        for index in range(len(nums)):
            if nums[index] in hash_map:
                return [hash_map[nums[index]],index]
            else:
                hash_map[target-nums[index]]=index

