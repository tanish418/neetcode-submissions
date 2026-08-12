class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        hmap1 = {}
        for c in s1:
            hmap[c]= hmap.get(c,0)+1
        l=0
        cond = len(s1)
        for r in range(len(s2)): 
            hmap1[s2[r]] = hmap1.get(s2[r],0)+1
            while r-l+1>cond and hmap1!=hmap:
                hmap1[s2[l]]-=1
                if hmap1[s2[l]]==0:
                    del hmap1[s2[l]]
                l+=1
            if hmap1 == hmap:
                return True
        return False               