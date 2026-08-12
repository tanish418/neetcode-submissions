from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Extract the original string
            decoded.append(s[j + 1 : j + 1 + length])

            # Move to the next encoded string
            i = j + 1 + length

        return decoded