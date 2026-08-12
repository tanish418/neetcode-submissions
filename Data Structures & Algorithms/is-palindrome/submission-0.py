import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        s = re.sub(r'[^a-zA-Z0-9 ]', '', s)
        s = s.lower().replace(" ","" )
        print(s)
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True            