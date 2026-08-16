class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dictt=set()

        for i in nums:
            if i not in dictt:
                dictt.add(i)
        countt=0
        bestcount=0
        for i in nums:
            if i-1 not in dictt:
                countstart=i
                countt=1
                while countstart+1 in dictt:
                    countstart=countstart+1
                    countt+=1
                bestcount=max(countt,bestcount)
        return bestcount
              
        
        ## we need to use set insteadd ok - atttemp 3
        # dictt={}
        # for i in nums:
        #     dictt[i]

        
        
        ##attempt 2
        # nums.sort()
        # print(nums)
        # nextvalu=nums[0]+1
        # countt=1
        # for i in range(len(nums)):
        #     if nums[i]==nextvalu:
        #         nextvalu=nextvalu+1
        #         countt+=1
        # return nextvalu





        ## attempt 1

        # i=1
        # if len(nums)==0:
        #     return 0
        # curr=nums[0]
        # cou=1
        # print(i,"next checking index")
        # print(curr,"current val - next")
        # print(cou,"s count")
        # print()
        # while i<len(nums):
        #     if nums[i]==curr+1:
        #         print("nums[i]==curr+1",nums[i],curr+1)
        #         i+=1
        #         curr=curr+1
        #         cou+=1
        #         print(i,"next checking index")
        #         print(curr,"streak continue - next")
        #         print(cou,"s count")
        #         print()
        #     else:
        #         i+=1
        # return cou

        # i=1
        # curr=nums[0]
        # while i<len(nums):
        #     if -1==-1+1:
        #         cou+=1
        #         i+=1 ##3
        #         curr=-1+1
        #     else:
        #         i+=1
            

        