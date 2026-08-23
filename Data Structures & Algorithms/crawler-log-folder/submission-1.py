class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for c in logs:
            if c =="../":
                count-=1
            elif c=="./":
                count+=0
            else:
                count+=1
        return count if count>0 else 0                