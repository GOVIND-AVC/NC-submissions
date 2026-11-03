class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dictt={}
        lenn=t
        maxsub=""
        for i in range(len(t)):
            if t[i] not in dictt:
                dictt[t[i]]=1
            else:
                dictt[t[i]]+=1
        print(dictt)

        # i=0
        # tempdictt={}
        # while i<len(s):
        #     if s[i] not in tempdictt:
        #         tempdictt[s[i]]=1
        #     else:
        #         tempdictt[s[i]]+=1
        #     i+=1
        # print(tempdictt)

        i=0
        j=0
        mnlngth=float('inf')
        currstr=""
        newdictt={}
        cnt=0
        while j<len(s):
            if s[j] not in dictt:
                j+=1
            else:
                if s[j] not in newdictt:
                    newdictt[s[j]]=1
                else:
                    newdictt[s[j]]+=1
                if newdictt.get(s[j],0)<=dictt.get(s[j],0):
                    cnt+=1
                    if cnt==len(t):
                        while cnt>=len(t):
                            lngth=(j-i)+1
                            if mnlngth>lngth:
                                mnlngth=lngth
                                currstr=s[i:j+1]
                            if s[i] not in dictt:
                                i+=1
                            else:
                                if newdictt.get(s[i],0)<=dictt.get(s[i],0):
                                    cnt-=1
                                newdictt[s[i]]-=1
                                i+=1
                j+=1
                
        print(currstr)


        return currstr
        

















        # while j<len(s):
        #     if s[j] not in dictt:
        #         j+=1
        #     else:
        #         if s[j] in newdictt:
        #             newdictt[s[j]]+=1
        #             cnt+=
        #         else:
        #             newdictt[s[j]]=1
        #         if 
        #             lng=(j-i)+1
        #             if lng<mnlngth:
        #                 mnglngth=lng
                    
        #         j+=1
        # print(mnglngth)
                





        ## again-afterwrds-----                
            
        # print(dictt)

        # tempdictt={}

        # i=0
        # j=0
        # cnt=0
        # while j<len(s):
        #     # if cnt!=len(t):
        #     if s[j] not in tempdictt:
        #         tempdictt[s[j]]=1
        #         if s[j] in dictt:
        #             cnt+=1
        #     else:
        #         k=tempdictt.get(s[j],0)
        #         p=dictt.get(s[j],0)
        #         print(k,p)
        #         print()
        #         if k<p:
        #             cnt+=1
        #         tempdictt[s[j]]+=1
        #     j+=1
        # print(tempdictt)
        
        # while i<(j-i)+1:
        #     k=tempdictt[s[i]]
        #     m=tempdictt.get(k,0)
        #     print(i)
        #     if k in dictt:
        #         print("trrr")
        #     if k in dictt:
        #         p=dictt.get(k,0)
        #         if p<m:
        #             tempdictt[s[i]]-=1
        #             if tempdictt[s[i]]==0:
        #                 del tempdictt[s[i]]
        #         else:
        #             i+=1
        #     else:
        #         i+=1
        # print(tempdictt)

        ## after this i-fixed then check from the right side once again - till the window size is  valid ..?

                    
                






















# -- intialapproachh
# what we need to do
# we need to get the substrings - thats 1.. before that we need the track of every characters in t - incl dupl
# SO it will be like - 
# a susbtring - is fine - if that substring - contains - all values of t
# so definitely - that substring should contain min length - that is the length of t
# which so - we can proceed - with fixed size sliding window of length min n
# So here - we can see that  using fixed sized sliding winddow.. might not give us the correct output
# See - we can see that - in the given example - susbtrign - they have given as the output is YXAZ - and the t is XYZ - so obviously the len of the window will be greater that or equal to t - thats one - but another thing we can assume here - 
# if we are on the way generating each substrings - then - 
# see we can move the right pointer till the end and if characters are there - then we can just return it right -
# But the required output is the shortest substring right -
# so on the way - getting the susbtring - we can check - that on each min - window size
# that is if we start from 0 in the given example - we need to go atleast till - size of the t
# So - it will be like - 0 to that is i -> i+3 -1 -> so we have OUZ -> but we can check if each character in the string thats atleast one key matches the dict of T
# if not  - we can move the i to where j+1 is there currently -> then again increase the 
# j to i+3 -1 so it will be -> ODY so here -> we can see Y is there -> so we start increasing the right pointer +1 -> meanwhile check in the left window -> is a character thats present in the other dictt-> if not -> we increase the I also
# so its -> 
# ODY -> DYX 
# then again check -> 
# YXA ->minsize->T -> so incr-> j -> but when we check i-> its a character its there in the dictt
# so -> dont move i -> so now -> YXAZ -> then we check -> so we now have the windowsize>=sizet right
# SO - we can check - and if its present -> we can return that string from ito j+1 right..
        