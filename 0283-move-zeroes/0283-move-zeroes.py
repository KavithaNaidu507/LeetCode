class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        index=0
        temp=[0]*n 
        for i in range(n):
            if nums[i]!=0:
                temp[index]=nums[i]
                index+=1 
        for i in range(n):
            nums[i]=temp[i]
        return nums