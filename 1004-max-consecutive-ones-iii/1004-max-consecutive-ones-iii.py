class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        ans=0
        zeroes=0
        left=0
        n=len(nums)
        for right in range(n):
            if nums[right]==0:
                zeroes+=1
            if zeroes>k:
                if nums[left]==0:
                    zeroes-=1
                left+=1
        ans=max(ans,right-left+1)
        return ans