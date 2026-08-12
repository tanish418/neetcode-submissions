class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        minIndex= []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]+nums[j] == target and i!=j:
                    if len(minIndex)==0:
                        minIndex = [i,j]
                    else:
                        minIndex = min(minIndex,[i,j])    
        return minIndex            