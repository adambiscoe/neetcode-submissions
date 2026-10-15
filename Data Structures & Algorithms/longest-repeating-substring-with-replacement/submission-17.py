class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        beg = 0
        end = 0
        maxLen = 0
        currLen = 0
        mostFreqLetterCount = 0
        while end < len(s):
            # if the total window is less or equal to most freq letter plusk, keep increasing the end and update
            if s[end] not in hashMap:
                hashMap[s[end]] = 1;
            else:
                hashMap[s[end]] += 1
            if hashMap[s[end]] > mostFreqLetterCount:
                mostFreqLetterCount = hashMap[s[end]]
            currLen = end - beg + 1
            if mostFreqLetterCount + k >= currLen:
                if currLen > maxLen:
                    maxLen = currLen
                end += 1      
            else:
                while mostFreqLetterCount + k < end - beg + 1:
                    hashMap[s[beg]] -= 1
                    beg += 1
                end += 1
        return maxLen




        
       


        



            
            



        