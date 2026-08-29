class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        dictt={}
        maxcount=0

        while j<len(s):
            if s[j] not in dictt:
                dictt[s[j]]=1
            else:
                while s[j] in dictt:
                    dictt[s[i]]-=1

                    if dictt[s[i]]==0:
                        del dictt[s[i]]
                    
                    i+=1
                dictt[s[j]]=1

            maxcount=max(maxcount,len(dictt))
            j+=1
        
        return maxcount

























        # while j<len(s):
        #     if s[j] not in dictt:
        #         dictt[s[j]]=1
        #     else:
        #         while s[j] in dictt: ## dictt[s[j]] in dict -- meaning - value of this , and s[j] in dictt - key of this

        #             dictt[s[i]]-=1

        #             if dictt[s[i]]==0:
        #                 del dictt[s[i]]
                    
        #             i+=1
        #         dictt[s[j]]=1
        #     maxcount=max(maxcount,len(dictt))
        #     j+=1
        # return maxcount
            

        



### attempt - 1 -- tried different complex way of counting - like instead of just incrementing the counter to 2 - tried optimizing without that --

          # i=0
#         j=0
#         dictt={}
#         maxcount=0
#         while j<len(s):
#             if s[j] not in dictt:
#                 dictt[s[j]]=1
#                 if len(dictt)>maxcount:
#                     maxcount=len(dictt)
#                 # print(dictt)
#             else:
#                 while dictt[s[j]]:
#                     dictt[s[i]]-=1
#                     if dictt[s[i]]==0:
#                         del dictt[s[i]]
#                         i+=1
#                         break
#                     # if dictt[s[i]]==0:
#                     #     del dictt[s[i]]
#                 # i+=1
#                 dictt[s[j]]=1
#                 if len(dictt)>maxcount:
#                     maxcount=len(dictt)
#                 # print(dictt)
#                 # print(len(dictt))

#                 # dictt[s[j]]+=1
#             j+=1
#         # print(dictt)
#         return maxcount
    

        