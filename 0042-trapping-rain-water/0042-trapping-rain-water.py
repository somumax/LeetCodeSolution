class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftToright = [0]*len(height)
        rightToleft = [0]*len(height)
        #left to right find max
        leftToright[0] = height[0]
        for i in range(1,len(height)):
            leftToright[i] = max(leftToright[i-1],height[i])

        #right to left find max
        rightToleft[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            rightToleft[i] = max(rightToleft[i+1],height[i])
        
        #find min ltor & rtoleft subtract height and res 
        for i in range(len(height)):
            res += (min(leftToright[i],rightToleft[i])-height[i])
        
        return res
        
        
