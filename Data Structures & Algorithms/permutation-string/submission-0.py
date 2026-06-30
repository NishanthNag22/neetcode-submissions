class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        s1_freq=[0]*26
        window_freq=[0]*26
        
        for i in range(n1):
            s1_freq[ord(s1[i])-ord('a')]+=1
            window_freq[ord(s2[i])-ord('a')]+=1

        if s1_freq==window_freq:
            return True
        for i in range(n1,n2):
            window_freq[ord(s2[i])-ord('a')]+=1
            window_freq[ord(s2[i-n1])-ord('a')]-=1
            if s1_freq==window_freq:
                return True
        return False