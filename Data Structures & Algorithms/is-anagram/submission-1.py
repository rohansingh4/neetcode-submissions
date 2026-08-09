class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for ch in s:
            if ch in sDict:
                sDict[ch] += 1
            else:
                sDict[ch] = 1
        for chh in t:
            if chh in tDict:
                tDict[chh] += 1
            else:
                tDict[chh] = 1
        return sDict == tDict