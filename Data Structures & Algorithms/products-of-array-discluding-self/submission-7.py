class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        prefix.append(1)
        for i in nums:
            prefix.append(prefix[-1]*i)
            # print(prefix)
        prefix=prefix[:len(prefix)-1]
        # print(prefix)

        suffix=[]
        suffix.append(1)

        i=len(nums)-1
        while i>=0:
            suffix.append(suffix[-1]*nums[i])
            i-=1
            # print(suffix)
        suffix=suffix[:len(suffix)-1]
        suffix=suffix[::-1]
        # print(suffix)
        fin=[]
        for i in range(len(nums)):
            fin.append(suffix[i]*prefix[i])
        # print(fin)
        return fin







        
        
        #attempt - 2 - TLE - suffix - taking O(n^2) -  reduce that by starting from the right
        # prefix=[]
        # prefix.append(1)
        # for i in nums:
        #     prefix.append(prefix[-1]*i)
        #     # print(prefix)
        # prefix=prefix[:len(prefix)-1]
        # # print(prefix)

        # suffix=[]
        # suffix.append(1)
        # # print(nums)
        # i=0
        # while i<len(nums):
        #     j=i+1
        #     prdc=1
        #     while j>i and j<len(nums):
        #         prdc*=nums[j]
        #         j+=1
        #     suffix.append(prdc)
        #     i+=1
        #     # print(suffix)
        # suffix=suffix[1:]
        # # print(suffix)

        # fin=[]
        # for i in range(len(nums)):
        #     fin.append(prefix[i]*suffix[i])
        # # print(fin)
        # return fin

        # # for i in range(-1,(len(nums)*-1),-1):
        # #     # l=len(suffix)
        # #     print(i)
        # #     suffix.append(suffix[-1]*nums[i])
        # #     print(suffix)

        

        # attempt - 1 - TLE
        # fin=[]
        # for i in range (len(nums)):
        #     curr=1
        #     for j in range (len(nums)):
        #         if i!=j:
        #             curr=curr*nums[j]
        #     fin.append(curr)
        # return fin

            
        