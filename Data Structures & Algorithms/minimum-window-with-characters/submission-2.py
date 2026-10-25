class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tMap = {}
        winMap = {}
        for i in range(len(t)):
            if t[i] in tMap:
                tMap[t[i]] += 1
            else:
                tMap[t[i]] = 1
        need = len(tMap)
        have = 0
        beg = 0
        end = 0
        minLen = float("infinity")
        fullWindow = False
        minBeg = 0
        minEnd = 0
        while(end < len(s)):
            ## if no window yet and a searched for char found
            if s[end] in winMap:
                winMap[s[end]] += 1
            else:
                winMap[s[end]] = 1
            if s[end] in tMap and tMap[s[end]] == winMap[s[end]]:
                have += 1
            while have == need:
                if end - beg + 1 < minLen:
                    minLen = end - beg + 1
                    minBeg = beg
                    minEnd = end
                winMap[s[beg]] -= 1
                if s[beg] in tMap and winMap[s[beg]] < tMap[s[beg]]:
                    have -= 1
                beg += 1
            end += 1
        if minLen == float("infinity"):
            return ""
        return s[minBeg:minEnd + 1]







        
        