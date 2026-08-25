class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        ans=1
        seen=set(nums)
        for num  in seen:
            if num -1 not in seen:
                count=1 
                while num+count in seen:
                    count+=1 
                ans=max(ans,count)
        return ans