class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn=float("inf")
        for i in nums:
            minn=min(i,minn)
        return minn    