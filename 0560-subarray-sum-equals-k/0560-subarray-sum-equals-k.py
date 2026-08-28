class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref=0
        count=0
        freq={0:1}
        for num in nums:
            pref+=num 
            count+=freq.get(pref-k,0)
            freq[pref]=freq.get(pref,0)+1 
        return count