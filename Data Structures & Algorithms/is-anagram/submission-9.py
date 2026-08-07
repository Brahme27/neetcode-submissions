class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            arr=[0]*266
            for i in range(len(s)):
                arr[ord(s[i])]+=1
                arr[ord(t[i])]-=1
            
            for num in arr:
                if num!=0:
                    return False
            return True