class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set={}
        x=list()
        for i in range(len(nums)):
            if nums[i] not in nums_set:
                nums_set[nums[i]]=0
            nums_set[nums[i]]+=1
        sorted_pairs=sorted(nums_set.items(),key=lambda item:item[1],reverse=True)
        for i in range(k):
            x.append(sorted_pairs[i][0])
        return x