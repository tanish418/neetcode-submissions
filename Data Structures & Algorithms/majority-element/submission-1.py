import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash1 = {}
        for num in nums:
            hash1[num] = hash1.get(num, 0) + 1
        max_val = -math.inf
        index = 0
        for key in hash1:
            if hash1[key] > max_val:
                max_val = hash1[key]
                index = key     
        return index