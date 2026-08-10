class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}

        for i in strs:
            key="".join(sorted(i))
            
            if key in dictt:
                dictt[key].append(i)
            else:
                dictt[key]=[i]

        fin=list(dictt.values())
        # print(fin)
        return fin
        

        

        






        
        # dictt={}

        # for i in strs:
        #     key="".join(sorted(i))
        #     if key not in dictt:
        #         dictt[key]=[i]
        #     else:
        #         dictt[key].append(i)

        # # print(dictt)
        # fin=[]
        # for i in dictt.values():
        #     fin.append(i)
        # # print(fin)
        
        # # fin=list(dictt.values())

        # return fin
            


        # strs.sort()
        # print(strs)
        # store={}
        # fin=[]
        # sortd=[]
        # for i in strs:
        #     j=sorted(i)
        #     sortd.append(j)
        # print(sortd)

        # i=0
        # while i<len(sortd):
        #     if len(fin)==0:
        #         fin.append(sortd[i])
        #         i+=1
        #     else:
        #         if fin[-1]==sortd[i]:
        #             fin[-1].append(sortd[i])
        #             i+=1
        #         else:
        #             fin.append(sortd[i])
        #             i+=1
        # print(fin)
        
            