class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0,len(nums)):
            
            req = target - nums[i]
            if req in seen:
            
                if seen[req]!= i:
                    return [seen[req],i]    
            if nums[i] not in seen:
                seen.update({nums[i]:i});        