class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash= [0]*10**5
        for i in range(0,len(nums)):
            hash[nums[i]] += 1

        for i in range(0,len(nums)):
            if hash[nums[i]]>=2:
                return True
        return False         
        