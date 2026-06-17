class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_sorted=sorted(s)
        t_sorted=sorted(t)
        for i in range(len(s)):
            if s_sorted[i-1]!=t_sorted[i-1]:
                return False
        return True