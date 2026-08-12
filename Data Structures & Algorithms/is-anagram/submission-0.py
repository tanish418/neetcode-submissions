class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #declare two hash
        hash1=[0]*26
        hash2=[0]*26

        #precompute number of characters 
        for ch in s:
            hash1[ord(ch)-ord('a')] +=1
        for ch in t:
            hash2[ord(ch)-ord('a')] +=1
        

        #match both has if same return true else false 
        if hash1 == hash2:
            return True
        else:
            return False    