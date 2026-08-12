class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r = 1,max(piles)

        while l<=r:
            t_hour=0
            mid = l+(r-l)//2
            for pile in piles:
                t_hour+=(pile+mid-1)//mid
                if t_hour>h:
                    break
            
            if t_hour>h:
                l=mid+1
            else:
                r=mid-1
        return l                