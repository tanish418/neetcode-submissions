class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        l_f = len(word1)
        r=0
        r_f = len(word2)
        merge =[]

        while l<l_f and r<r_f:
            merge.append(word1[l])
            merge.append(word2[r])
            l+=1
            r+=1
        while l<l_f:
            merge.append(word1[l])
            l+=1
        while r<r_f:
            merge.append(word2[r])
            r+=1

        return "".join(merge)