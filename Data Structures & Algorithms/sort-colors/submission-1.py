class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''flag = True
        n = len(nums)
        while flag:
            flag=False
            for j in range(1,n):
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                    flag = True
        '''
        maxx = 2
        count = [0]*3
        for num in nums:
            count[num]+=1
        i=0
        for c in range(maxx+1):
            while count[c]>0:
                nums[i]=c
                i+=1
                count[c]-=1    
