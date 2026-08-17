class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        n=len(nums)
        for i in range(n):
            arr.append((nums[i],i))
        arr.sort()
        left=0
        right=n-1
        while left<right:
            sum=arr[left][0]+arr[right][0]
            if sum==target:
                return arr[left][1],arr[right][1]
            elif sum>target:
                right-=1
            else:
                left+=1
        return []