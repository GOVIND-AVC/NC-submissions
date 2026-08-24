class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[]
        currbig=height[0]
        for i in range(len(height)):
            leftmax.append(currbig)
            if height[i]>currbig:
                currbig=height[i]
        # print(height)
        # print(leftmax)
        rightmax=[]
        currbig=height[-1]
        for i in range(len(height)-1,-1,-1):
            rightmax.append(currbig)
            if height[i]>currbig:
                currbig=height[i]
        rightmaxnew=rightmax[::-1]
        # print(rightmaxnew)    
        maxstore=0
        for i in range(len(height)):
            currentpossible=min(leftmax[i],rightmaxnew[i])-height[i]
            if currentpossible >0:
                maxstore+=currentpossible
            # print(maxstore)
        return maxstore




