class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l=max(weights)
        minn=float("inf")
        while l<=r:
            cap = l+(r-l)//2
            t_days=1
            curr_weight = 0
            for weight in weights:
                if curr_weight+weight<=cap:
                    curr_weight+=weight     
                
                elif curr_weight+weight>cap:
                    t_days+=1
                    curr_weight=weight

            if t_days >days:
                l=cap+1
            else:
                r=cap-1
        return l
            
