class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expsum=n*(n+1)//2
        actualsum=sum(nums)
        return expsum-actualsum