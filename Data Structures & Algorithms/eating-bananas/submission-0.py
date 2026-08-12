class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        l=1
        hour=[]
        while l<=r:
            mid = l+(r-l)//2
            hour= [math.ceil(pile/mid) for pile in piles ]
            t_hour = sum(hour)
            if t_hour<=h:
                r = mid-1
            else: 
                l= mid + 1
        return l

        