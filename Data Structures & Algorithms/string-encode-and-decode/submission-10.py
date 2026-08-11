class Solution:
    def encode(self, strs: List[str]) -> str:
        st=""
        for i in strs:
            # print(i,len(i))
            st+=str(len(i))+"#"+i
            # print(st)
        return st
        # return self.decode(st)
        
    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        fin=[]
        sr=""
        # print(s)
        def findcurrentstringlength(i):
            num=""
            while i<len(s):
                if s[i]!="#":
                    num+=s[i]
                    # print(num,"Inside lenfinder function")
                    i+=1
                else:
                    return num
            
        currlen=int(findcurrentstringlength(0))
        i=len(str(currlen))+1
        if currlen==0:
            fin.append(sr)

        while i<len(s):
            sr=""
            while currlen>0:
                sr+=s[i]
                # print(i,s[i],"current i index of S")
                # print(currlen,"currlen of the word")
                currlen-=1
                if currlen !=0:
                    i+=1
                else:
                    i+=1
                    fin.append(sr)
                    # print()
            if i<len(s):
                currlen=int(findcurrentstringlength(i))
                if currlen==0:
                    fin.append("")
            i+=len(str(currlen))+1
            # print(fin)
        return fin

        

            


        # currlen=int(s[0])
        # i=1
        # print(s)
        # while i<len(s)+1:
        #     sr=""
        #     while currlen>0:
        #         sr+=s[i]
        #         # print(sr,"already printed inside loop")
        #         # print(i,"current i pointer")
        #         # print(currlen,"currlen")
        #         currlen-=1
        #         if currlen!=0:
        #             i+=1
        #         else:
        #             fin.append(sr)
        #             i+=1
        #     # print(fin) 
        #     # print(s[i],"after first word,next pointer on s")
        #     if i<len(s):
        #         currlen=int(s[i])
        #     i+=1
        #     print(fin)
        #     # print(currlen)
            
        #         # print(sr)
        #     # print(sr)
        #     # print(fin)
        # return fin

## 3rd attempt
# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         st=""
#         for i in strs:
#             # print(i,len(i))
#             st+=str(len(i))+i
#             # print(st)
#         return self.decode(st)
        
#     def decode(self, s: str) -> List[str]:
#         fin=[]
#         sr=""
#         currlen=int(s[0])
#         i=1
#         print(s)
#         while i<len(s)+1:
#             sr=""
#             while currlen>0:
#                 sr+=s[i]
#                 # print(sr,"already printed inside loop")
#                 # print(i,"current i pointer")
#                 # print(currlen,"currlen")
#                 currlen-=1
#                 if currlen!=0:
#                     i+=1
#                 else:
#                     fin.append(sr)
#                     i+=1
#             # print(fin) 
#             # print(s[i],"after first word,next pointer on s")
#             if i<len(s):
#                 currlen=int(s[i])
#             i+=1
#             print(fin)
#             # print(currlen)
            
#                 # print(sr)
#             # print(sr)
#             # print(fin)
#         return fin

    
    ##2nd attempt
    # def encode(self, strs: List[str]) -> str:
    #     st=""
    #     for i in strs:
    #         print(i,len(i))
    #         st+=str(len(i))+i
    #         print(st)
    #     return self.decode(st)
        
    # def decode(self, s: str) -> List[str]:
    #     fin=[]
    #     sr=""
    #     for i in range(len(s)):
    #         if s[i]=="!":
    #             fin.append(sr)
    #             sr=""
    #         else:
    #             sr+=s[i]
    #             # print(sr)
    #         # print(sr)
    #         # print(fin)
    #     return fin

    # global fin
    # fin=[]
    # def encode(self, strs: List[str]) -> str:
    #     for i in strs:
    #         self.decode(i)
    #     global j
    #     j=len(strs)
    # def decode(self, s: str) -> List[str]:
    #     fin.append(s)
    #     if len(fin)==j:
    #         return fin
    # def ret(fin):
    #     return fin