class Solution:
    def alphaNum(self,c):
        return(ord('A')<=ord(c)<=ord('Z')) or (ord('a')<=ord(c)<=ord('z')) or (ord('0')<=ord(c)<=ord('9'))               
    def isPalindrome(self, s: str) -> bool:
        """i=0
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
        return True    """
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1 
            while l<r and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True