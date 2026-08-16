class Solution:
    def isPalindrome(self, s: str) -> bool:
        stt=""
        for i in range(len(s)):
            if s[i].isdigit() or s[i].isalpha():
                stt+=s[i].lower()

        # print(stt)

        i=0
        j=len(stt)-1
        while i<=j:
            if stt[i]==stt[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        