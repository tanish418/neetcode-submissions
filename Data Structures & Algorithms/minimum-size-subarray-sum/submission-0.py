class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        summ = 0
        minn = float("inf")
        flag = False
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                flag=True 
                minn = min(minn, r - l + 1)
                summ -= nums[l]
         
                l += 1
        if flag:        
            return minn      
        else: return 0      