from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = Counter(s)
        check2 = Counter(t)
        return check1==check2