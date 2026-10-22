class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dictt={}
        for i in range(len(s1)):
            if s1[i] not in dictt:
                dictt[s1[i]]=1
            else:
                dictt[s1[i]]+=1

        windowsize=len(s1)

        tempdict={}
        i=0
        j=0
        while j<len(s2):
            if s2[j] not in tempdict:
                tempdict[s2[j]]=1
            else:
                tempdict[s2[j]]+=1
            if ((j-i)+1)==windowsize:
                if tempdict==dictt:
                    return True 
                else:
                    tempdict[s2[i]]-=1
                    if tempdict[s2[i]]==0:
                        del tempdict[s2[i]]
                    i+=1
            j+=1
        return False
            

        