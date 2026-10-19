class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        beg = 0
        end = k
        ret = []
        window = {}
        for i in range(0, k):
            if nums[i] in window:
                window[nums[i]] += 1
            else:
                window[nums[i]] = 1
        maxVal = max(window.keys())
        print(window)
        ret.append(maxVal)
        while end < len(nums):
            if nums[end] in window:
                window[nums[end]] += 1
            else:
                window[nums[end]] = 1
            window[nums[beg]] -= 1
            if window[nums[beg]] == 0:
                window.pop(nums[beg])
            maxVal = max(window.keys())
            ret.append(maxVal)
            beg += 1
            end += 1

        
            

            
            
        

        return ret
            

        