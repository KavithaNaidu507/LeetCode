class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x 
        ans=0
        while x>0:
            digit=x%10
            ans=(ans*10)+digit 
            x//=10
        if ans==temp:
            return True 
        else:
            return False