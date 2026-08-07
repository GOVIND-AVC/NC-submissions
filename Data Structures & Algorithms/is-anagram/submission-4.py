class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tota={}
        for i in s:
            if i in tota:
                tota[i]+=1
            else:
                tota[i]=1
        
        for i in t:
            if i in tota:
                tota[i]-=1
                if tota[i]==0:
                    del tota[i]
            else:
                return False
        if not tota:
            return True
        else:
            return False
        