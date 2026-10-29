class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        rightEnd = nums[r]
        leftEnd = nums[0]
        prevCenter = -2000
        while l <= r:
            center = l + (r - l) // 2
            if nums[center - 1] > nums[center]:
                return nums[center]
            if nums[center] > rightEnd:
                l = center + 1
            else:
                r = center - 1
        return nums[r]




            

        