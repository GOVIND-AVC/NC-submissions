class Solution:
    def trap(self, height: List[int]) -> int:
        
        ## so here min(left,right)-height[i]
        ## to get this - min(left,right) -- is giving the bottleneck right -
        ## if left is smaller example - min(4,5) - then water level can exceed 4 right
        ## but so we try adjusting the smaller boundary 
        ## its like - we will process the side that is currently limiting the boundary i
        ## already know
        ##Process the side whose maximum is currently the limiting boundary, because its
        ##trapped water can already be determined safely.

        i=0
        j=len(height)-1
        currleftbig=height[0]
        curr_rightbig=height[-1]
        current_count=0
        tot=0
        # print(height)
        while i<=j:
            if currleftbig<=curr_rightbig:
                current_count=min(currleftbig,curr_rightbig)-height[i]
                if height[i]>currleftbig:
                    currleftbig=height[i]
                i+=1
            else:
                current_count=min(currleftbig,curr_rightbig)-height[j]
                if height[j]>curr_rightbig:
                    curr_rightbig=height[j]
                j-=1
            
            if current_count>0:
                tot+=current_count
        return tot

            



        ## attempt 2 - Prblm with this - See using this approach - 
        ## standing at a particular i - we donot know the maximum of both the ends yet
        ## initially assummed that - we are taking the maximum - but its not!!
        # i=0
        # j=len(height)-1
        # currleftbig=height[0]
        # curr_rightbig=height[-1]
        # current_count=0
        # tot=0
        # print(height)
        # while i<=j:
        #     print(currleftbig,curr_rightbig)
        #     current_count=min(currleftbig,curr_rightbig)-height[i]
        #     if height[i]>currleftbig:
        #         currleftbig=height[i]
        #     if height[j]>curr_rightbig:
        #         curr_rightbig=height[j]
        #     i+=1
        #     j-=1
        #     if current_count>0:
        #         tot+=current_count
        # return tot
            

            



## attempt - 1 -- O(n) TC and SC - using prefix/suffix like approach
        # leftmax=[]
        # currbig=height[0]
        # for i in range(len(height)):
        #     leftmax.append(currbig)
        #     if height[i]>currbig:
        #         currbig=height[i]
        # # print(height)
        # # print(leftmax)
        # rightmax=[]
        # currbig=height[-1]
        # for i in range(len(height)-1,-1,-1):
        #     rightmax.append(currbig)
        #     if height[i]>currbig:
        #         currbig=height[i]
        # rightmaxnew=rightmax[::-1]
        # # print(rightmaxnew)    
        # maxstore=0
        # for i in range(len(height)):
        #     currentpossible=min(leftmax[i],rightmaxnew[i])-height[i]
        #     if currentpossible >0:
        #         maxstore+=currentpossible
        #     # print(maxstore)
        # return maxstore




