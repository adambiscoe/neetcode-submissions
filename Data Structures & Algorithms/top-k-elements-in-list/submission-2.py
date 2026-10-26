class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##list of length k
        ## heap somewhere
        map = {}
        ret =[]
        for i in nums:
            if i in map:
                map[i] = map[i] + 1
            else:
                map[i] = 1
        newMap = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        keys = list(newMap.keys())
        catch = 0
        for i in range(len(keys)):
            ret.append(keys[i])
            catch = catch + 1
            if catch == k:
                break
        return ret


        