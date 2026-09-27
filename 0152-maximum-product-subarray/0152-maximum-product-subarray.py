class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax,curmin=1,1
        res=nums[0]
        for n in nums:
            vals=(n,n*curmax,n*curmin)
            curmin,curmax=min(vals),max(vals)
            res=max(res,curmax)
        return res