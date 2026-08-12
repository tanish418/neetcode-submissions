from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = {}

        for stri in strs:
            hash1 = [0] * 26

            for ch in stri:
                hash1[ord(ch) - ord('a')] += 1

            hash1 = tuple(hash1)

            if hash1 in dicti:
                dicti[hash1].append(stri)
            else:
                dicti[hash1] = [stri]

        return list(dicti.values())