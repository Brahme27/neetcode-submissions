class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)   
        if len(s)!=len(t):
            return False
        count=[0]*256  
        for i in range(len(s)):
            count[ord(s[i])]+=1 
            count[ord(t[i])]-=1

        for num in count:
            if num!=0:
                return False
        return True
