class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        ans=[]
        count1,count2,count3=0,0,0
        for num in nums:
            if num==0:
                count1+=1
            elif num==1:
                count2+=1
            else:
                count3+=1
        i=0
        while count1>0:
            nums[i]=0 
            i+=1
            count1-=1
        while count2>0:
            nums[i]=1
            i+=1
            count2-=1
        while count3>0:
            nums[i]=2
            i+=1
            count3-=1