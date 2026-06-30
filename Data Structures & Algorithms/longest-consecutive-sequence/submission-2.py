class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n=len(nums)
        count=1
        maxCount=0
        for i in range(1,n):
            diff=nums[i]-nums[i-1]
            if diff==0:
                continue
            if diff==1:
                count+=1
            else:
                maxCount=max(count,maxCount)
                count=1
        return max(maxCount,count)