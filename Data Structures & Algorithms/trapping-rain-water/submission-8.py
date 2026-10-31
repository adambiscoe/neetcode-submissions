class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        maxR = deque([])
        maxRVal = 0
        maxL = deque([])
        maxLVal = 0
        totalWater = 0
        while i < len(height):
            if height[i] > maxLVal:
                maxL.append(height[i])
                maxLVal = height[i]
            else:
                maxL.append(maxLVal)
            if height[len(height) - 1 - i] > maxRVal:
                maxR.appendleft(height[len(height) - 1 - i])
                maxRVal = height[len(height) - 1 - i]
            else:
                maxR.appendleft(maxRVal)
            i += 1
        for i in range(len(height)):
            totalWater += min(maxR[i], maxL[i]) - height[i]
        return totalWater
        
        

        
             
            

        

                
               
            


        