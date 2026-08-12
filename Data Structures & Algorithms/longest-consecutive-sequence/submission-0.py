class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashh = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in hashh:
                length=0
                while i+length in hashh:
                    length+=1
                longest = max(longest,length)    

        return longest 

                
        