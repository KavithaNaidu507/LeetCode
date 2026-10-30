class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        sum=0
        maxi=float('-inf')
        for i in range(k):
            sum+=nums[i]
        maxi=sum
        for i in range(k,n):
            sum+=nums[i]
            sum-=nums[i-k]
            maxi=max(maxi,sum)
        return maxi/k
