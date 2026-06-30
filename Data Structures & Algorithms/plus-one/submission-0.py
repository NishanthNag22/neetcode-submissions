class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        ans=[]
        n=len(digits)
        for i in range(n):
            number+=digits[i]
            number*=10
        number=number//10
        number+=1
        length=len(str(number))
        reverse=int(str(number)[::-1])
        dig=0
        for i in range(length):
            dig=reverse%10
            ans.append(dig)
            reverse=reverse//10
        return ans
