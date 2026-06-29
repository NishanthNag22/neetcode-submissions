class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i,j=0,n-1
        maxArea=0
        while i<j:
            diff=j-i
            minPole=min(heights[j],heights[i])
            area=minPole*diff
            if area>maxArea:
                maxArea=area
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        return maxArea