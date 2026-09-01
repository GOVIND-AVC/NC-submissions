class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        val=0
        while i<j:
            val=max(val,(j-i)*min(heights[i],heights[j]))
            if heights[i]>=heights[j]:
                j-=1
            elif heights[j]>=heights[i]:
                i+=1
        return val

# The shorted bar is limiting the height - if the left bar is shorter - move the left,
# If the right bar is shorted move the right - 
# that matters because we calculate the width * min(height[i],height[j])
## right - so more height - better - value 


## Attemp - 2  - TLE
#         i=0
#         j=1
#         val=0
#         while i<len(heights):
#             # if j>len(heights)-1:
#             #     break
#             # if heights[j]>heights[i]:
#             #     i=j
#             #     j=j+1
#             while j<=len(heights)-1:
#                 cwid=j-i
#                 # print(heights[i],heights[j])
#                 minh=min(heights[i],heights[j])
#                 val=max(val,minh*cwid)
#                 # print(val)
#                 # print()
#                 j+=1
#             i+=1
#             j=i+1
#         return val


#         ## Attempt - 1
#         # print(heights)
#         # i=0
#         # j=1
#         # val=0
#         # while i<len(heights):
#         #     if j>len(heights)-1:
#         #         break
#         #     if heights[j]>heights[i]:
#         #         i=j
#         #         j=j+1
#         #     else:
#         #         cwid=j-i
#         #         minh=min(heights[i],heights[j])
#         #         val=max(val,minh*cwid)
#         #         print(val)
#         #         j+=1
#         # return val



        