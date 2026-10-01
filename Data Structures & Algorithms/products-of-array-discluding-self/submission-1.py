class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        currPref = 1
        pref.append(currPref)
        post = deque()
        currPost = 1
        post.append(currPost)
        for i in range(len(nums) - 1):
            pref.append(currPref * nums[i])
            currPref *= nums[i]
        for i in range(len(nums) - 1, 0, -1):
            post.appendleft(currPost * nums[i])
            currPost *= nums[i]
        ret = []
        for i in range(len(nums)):
            ret.append(pref[i] * post[i])
        return ret
        