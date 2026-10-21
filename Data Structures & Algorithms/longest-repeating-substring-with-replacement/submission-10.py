class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        dictt={}
        maxlen=0

        while j<len(s):
            if s[j] not in dictt:
                dictt[s[j]]=1
            else:
                dictt[s[j]]+=1

            currwindowlen=(j-i)+1

            highref=max(dictt.values())

            replacements=currwindowlen-highref

            if replacements>k:
                dictt[s[i]]-=1
                i+=1
                currwindowlen=(j-i)+1

            if currwindowlen>maxlen:
                maxlen=currwindowlen
            
            j+=1

        return maxlen

            







        









        # i=0
        # j=0
        # dictt={}
        # maxlen=0


        # while j<len(s):
        #     if s[j] not in dictt:
        #         dictt[s[j]]=1
        #     else:
        #         dictt[s[j]]+=1

        #     currwindowlength=(j-i)+1
        #     highf=max(dictt.values())
        #     replacements=currwindowlength-highf
        #     if replacements>k:
        #         dictt[s[i]]-=1
        #         i+=1
        #         currwindowlength=(j-i)+1
        #     if currwindowlength >maxlen:
        #         maxlen=currwindowlength

        #     j+=1

        # return maxlen       
        
        
        
        
        
        
        
        
        
        
        ##attempt-1
        # i=0
        # j=0
        # dictt={}
        # currmaxx=0
        # while i<n:
        #     if s[j] not in dictt:
        #         s[j]=1
        #     else:
        #         s[j]+=1
        #     j+=1
        #     if (max(dictt.values())-k)>=0:
        #         lenn=max(dictt)-k
        #         if lenn>currmaxx:
        #             currmaxx=lenn
        #     else:
        #         i+=1
        #     if j>=len(s):
        #         j=i+1
        #         i+=1
        

            





















        ## so the question - 
        ## we have k number of replacements -
        ## so after doing the k replacement -  we need to caluclate the longest substring containing only one distincct character

        ## So the initial assumption or intuition is like
        ## We can use a slidining window - we can also use a dict to keep a track of the elements
        ## SO it will be like - we will be accepting each characters into the window starting from the left side
        ## Then yep we can introduce those characters to the dictionary as we proceed, we can keep a count of the-
        ## number of replacements left using k itself, Then yep when some different element comes for example
        # we start from the first element then take the second - if its diffferent - deduct one k - continue opening the
        # window towards right - ok so when the k ==0 and some different character comes - we can take the maxlength of 
        # the window and store it as the currentmax or something --  then repeat  this etc-- thereby taking 
        # the substrings right - .. but some clarifications or missing is like the substrings part like - will this approach - be suitable for checking in each and every substrings..? or lets see


        



































        # r=0
        # l=0
        # dictt={}
        # maxcount=0
        # while r<len(s):
        #     if s[r] not in dictt:
        #         dictt[s[r]]=1
        #     else:
        #         if          