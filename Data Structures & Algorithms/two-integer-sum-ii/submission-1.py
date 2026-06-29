class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=list()
        n=len(numbers)
        for i in range(n-1):
            for j in range(i+1,n):
                if numbers[i]+numbers[j]==target:
                    x.append(i+1)
                    x.append(j+1)

        return x    