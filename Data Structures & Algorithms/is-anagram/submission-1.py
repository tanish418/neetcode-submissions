class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #declare two hash
        hash1=[0]*26
        if len(s) != len(t):
            return False
        for ch in s:
            hash1[ord(ch)-ord('a')] +=1
        for ch in t:
            hash1[ord(ch)-ord('a')] -=1    
        
        return hash1 == [0] * 26 