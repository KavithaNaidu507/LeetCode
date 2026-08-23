class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        rev = 0
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp = temp // 10
        if x < 0:
            rev = -rev   
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev