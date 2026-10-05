class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        starters = []
        currSeq = 0
        maxSeq = 1
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if not nums[i] - 1 in setNums:
                starters.append(nums[i])

        for i in range(len(starters)):
            prev = starters[i]
            currSeq = 1
            while prev + 1 in setNums:
                currSeq = currSeq + 1
                if currSeq > maxSeq:
                    maxSeq = currSeq
                prev = prev + 1
        return maxSeq

        

        