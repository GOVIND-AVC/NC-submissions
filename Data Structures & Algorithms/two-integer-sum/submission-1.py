class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt={}

        for i in range(len(nums)):
            targ=target-nums[i]
            if targ in dictt:
                return [dictt[targ],i]
            else:
                dictt[nums[i]]=i
        

        # nums.sort()
        # i=0
        # j=len(nums)-1

        # while i<j:
        #     if nums[i]+nums[j]==target:
        #         return [i,j]
        #     elif nums[i]+nums[j]>target:
        #         j-=1
        #     elif nums[i]+nums[j]<target:
        #         i+=1
        

