class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=list()
        for i in range(len(nums)):
            pdt=1
            for j in range(len(nums)):
                if i==j:
                    continue
                pdt*=nums[j]
            x.append(pdt)
        return x