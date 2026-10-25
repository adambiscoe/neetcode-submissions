class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkIfKValid(k):
            hours = 0
            for pile in piles:
                hours += max(1, math.ceil(pile / k))
            if hours <=  h:
                return True
            return False
        l = 1
        r = max(piles)
        currMin = r
        while l <= r:
            check = l + (r - l) // 2
            if checkIfKValid(check):
                if check < currMin:
                    currMin =  check
                r = check - 1
            else:
                l = check + 1
        return currMin
        