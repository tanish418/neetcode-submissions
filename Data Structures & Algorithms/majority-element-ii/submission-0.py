class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        count = len(nums) // 3

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        li = []        
        for key,value in freq.items():
            if value>count:
                li.append(key)
        return li                