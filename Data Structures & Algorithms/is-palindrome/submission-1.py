class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystr=[i.lower() for i in s if i.isalnum()]
        low=0
        high=len(mystr)-1
        while low<=high:
            if mystr[low]!=mystr[high]:
                return False
            low+=1
            high-=1
        return True        