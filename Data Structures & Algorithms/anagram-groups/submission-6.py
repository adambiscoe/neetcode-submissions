class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        ret = []
        for i in range(len(strs)):
            curr = strs[i]
            currChars = [0] * 26
            for j in range(len(curr)):
                currChars[ord(curr[j]) - ord("a")] += 1
            tup = tuple(currChars)
            if tup in strMap:
                strMap[tup].append(strs[i])
            else:
                strMap[tup] = [strs[i]]
        return list(strMap.values())


        
        