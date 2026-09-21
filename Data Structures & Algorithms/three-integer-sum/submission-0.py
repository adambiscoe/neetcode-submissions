class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map = {}
        triplets = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                remainder = 0 - (nums[i] + nums[j])
                if remainder in map and not i == 0 and not j == 0 and not i == j :
                    remIdx = map[remainder]
                    if not remIdx == i and not remIdx == j:
                        check = [nums[i], nums[j], remainder]
                        check.sort()
                        if check not in triplets:


                            triplets.append(check)

            map[nums[i]] = i
        return triplets


        