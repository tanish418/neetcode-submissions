class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        prod=1
        for i in range(len(nums)):
            if i+1>=len(nums):
                break
            prod *=nums[i]
            output [i+1] = prod 
        prod=1
        output[0]=1
        for i in range(len(nums)-1,-1,-1):
            
            output[i] *=prod    
            prod *= nums[i]
        return output