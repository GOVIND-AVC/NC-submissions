class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictt={}

        for i in nums:
            if  i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        # print(dictt)

        # dicts=sorted(lambda x:dicts[-1])
        key=[]
        for i in dictt:
            key.append(i)
        # print(key,"keys")
        val=[]
        for i in dictt.values():
            val.append(i)
        # print(val,"vals")

        valsorted=sorted(val)
        # print(valsorted)
        topval=valsorted[len(valsorted)-k:len(valsorted)]

        # print(topval)
        res=[]
        
        for i in dictt:
            if dictt[i] in topval:
                res.append(i)
        # print(res)
        return res

        

        # Find the top K from the values list - then store the      index- of that - means - need the index of the top K numbers -
        # newdict={}
        # for i in range(len(val)):
        #     newdict[val[i]]=key[i]
        #     print(newdict,"loooping")
        #     # if val[i] not in newdict:
        #     #     newdict[val[i]]=key[i]
        #     # else:
        #     #     newdict[val[i]]=key[i]
        # print(newdict,"Reversed between keys and values-newdict")

        # fin=list(newdict)
        # fin.sort()
        # fin=fin[len(fin)-k:len(fin)+1]
        # print(fin,"Top repeated values(keys) in newdict")
        # res=[]
        # for i in fin:
        #     if i in newdict:
        #         res.append(newdict[i])
        #         print(res,"keys(values) of the newdict")
            
        # return res
        # newdictsorted=sorted(newdict)
        # print(newdictsorted)

        


        # topkIndex=[]
        # for i in range(len(val)):
        #     t=sorted(topkIndex)
        #     if val[i]>

        
        
        # dicts=sorted(dictt)
        # # print(dicts[len(dicts)-k:len(dicts)])
        # return dicts[len(dicts)-k:len(dicts)]