class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        n = len(nums)
        while flag:
            flag=False
            for j in range(1,n):
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                    flag = True
