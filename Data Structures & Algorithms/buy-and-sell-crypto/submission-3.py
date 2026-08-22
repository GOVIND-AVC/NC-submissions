class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        st=0
        i=0
        curr=prices[0]
        if len(prices)==0:
            return 0
        elif len(prices)==1:
            return 0
        while i<len(prices):
            curr=min(curr,prices[i])
            if prices[i]>=curr:
                val=prices[i]-curr
                st=max(st,val)
            i+=1
        return st

            # if prices[i]<=curr:
            #     st=max(prices[i]-curr)

            