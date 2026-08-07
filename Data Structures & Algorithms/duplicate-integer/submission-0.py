class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        dictt={}
        for i in nums:
            if i in dictt:
                if dictt[i]>=1:
                    return True
            else:
                dictt[i]=1

        print(dictt)
        return False

        # return False
        