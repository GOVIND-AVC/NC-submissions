class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        trip=[]
        for i in range(len(nums)):
            first=i
            curr=[]
            if i<=len(nums)-2:
                if i>0:
                    if nums[i]!=nums[i-1]:
                        st=i+1
                        ls=len(nums)-1

                        while st<ls:
                            if nums[first]+nums[st]+nums[ls]==0:
                                curr.append(nums[first])
                                curr.append(nums[st])
                                curr.append(nums[ls])
                                trip.append(curr)
                                curr=[]
                                st+=1
                                ls-=1
                                while st+1<=len(nums)-2 and nums[st]==nums[st-1]:
                                    st+=1
                                while ls-1>st and nums[ls]==nums[ls+1]:
                                    ls-=1
                            elif nums[first]+nums[st]+nums[ls]>0:
                                ls-=1
                            else:
                                st+=1
                elif i==0:
                    st=i+1
                    ls=len(nums)-1

                    while st<ls:
                        if nums[first]+nums[st]+nums[ls]==0:
                            curr.append(nums[first])
                            curr.append(nums[st])
                            curr.append(nums[ls])
                            trip.append(curr)
                            curr=[]
                            st+=1
                            ls-=1
                            while st+1<=len(nums)-2 and nums[st]==nums[st-1]:
                                st+=1
                            while ls-1>st and nums[ls]==nums[ls+1]:
                                ls-=1
                        elif nums[first]+nums[st]+nums[ls]>0:
                            ls-=1
                        else:
                            st+=1
        return trip




## attempt - 2

        # nums.sort()
        # print(nums)
        # trip=[]
        # for i in range(len(nums)):
        #     first=i
        #     curr=[]
        #     if i<=len(nums)-2:
        #         if i>0:
        #             if nums[i]!=nums[i-1]:
        #                 st=i+1
        #                 ls=len(nums)-1
        #                 while st<ls:
        #                     if nums[first]+nums[st]+nums[ls]==0:
        #                         curr.append(nums[first])
        #                         curr.append(nums[st])
        #                         curr.append(nums[ls])
        #                         trip.append(curr)
        #                         curr=[]
        #                         # st+=1
        #                         # ls-=1
        #                         if st+1<=len(nums)-2 and nums[st+1]!=nums[st]:
        #                             st+=1
        #                         if ls-1>st and nums[ls]!=nums[ls-1]:
        #                             ls-=1
        #                         while st+1<=len(nums)-2 and nums[st]==nums[st+1]:
        #                             st+=1
        #                         while ls-1>st and nums[ls]==nums[ls-1]:
        #                             ls-=1
        #                         # break
        #                         # break
        #                     elif nums[first]+nums[st]+nums[ls]>0:
        #                         ls-=1
        #                     else:
        #                         st+=1
        #                 # if curr:
        #                 #     trip.append(curr)

        #         elif i==0:
        #             st=i+1
        #             ls=len(nums)-1
        #             while st<ls:
        #                 if nums[first]+nums[st]+nums[ls]==0:
        #                     curr.append(nums[first])
        #                     curr.append(nums[st])
        #                     curr.append(nums[ls])
        #                     trip.append(curr)
        #                     curr=[]
        #                     # st+=1
        #                     # ls-=1
        #                     if st+1<=len(nums)-2 and nums[st+1]!=nums[st]:
        #                         st+=1
        #                     if ls-1>st and nums[ls]!=nums[ls-1]:
        #                         ls-=1
        #                     while st+1<=len(nums)-2 and nums[st]==nums[st+1]:
        #                         st+=1
        #                     while ls-1>st and nums[ls]==nums[ls-1]:
        #                         ls-=1
        #                         # break
        #                         # break
        #                 elif nums[first]+nums[st]+nums[ls]>0:
        #                     ls-=1
        #                 else:
        #                     st+=1

        #         # if curr:  
        #         #     trip.append(curr)  
        # return trip  




        









# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         print(nums)
#         trip=[]
#         for i in range(len(nums)):
#             first=i
#             curr=[]
#             if i<=len(nums)-2:
#                 st=i+1
#                 ls=len(nums)-1
#                 while st<ls:
#                     if nums[first]+nums[st]+nums[ls]==0:
#                         curr.append(nums[i])
#                         curr.appendd(nums[first])
#                         curr.append(nums[ls])
#                     elif nums[first]+nums[st]+nums[ls]>0:
#                         ls-=1
#                     else:
#                         st+=1
#             if curr:
#                 trip.append(curr)  
#         return trip  




        









