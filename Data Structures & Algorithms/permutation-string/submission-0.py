class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Letters = {}
        s2Letters = {}

        for i in range(len(s1)):
            if s1[i] in s1Letters:
                s1Letters[s1[i]] += 1
            else:
                s1Letters[s1[i]] = 1
            if s2[i] in s2Letters:
                s2Letters[s2[i]] += 1
            else:
                s2Letters[s2[i]] = 1
        if s1Letters == s2Letters:
                return True

        for i in range(len(s1), len(s2)):
            if s2[i] in s2Letters:
                s2Letters[s2[i]] += 1
            else:
                s2Letters[s2[i]] = 1
            start = i - len(s1)
            s2Letters[s2[start]] -= 1
            if s2Letters[s2[start]] == 0:
                s2Letters.pop(s2[start], None)
            if s1Letters == s2Letters:
                return True
        return False
            
        









        