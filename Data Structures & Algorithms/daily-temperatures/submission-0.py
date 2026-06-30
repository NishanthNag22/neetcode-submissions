class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for i,t in enumerate(temperatures):
            while stack and temperatures[i]>stack[-1][0]:
                stackTemp,stackInd=stack.pop()
                res[stackInd]=i-stackInd
            stack.append((t,i))
        return res