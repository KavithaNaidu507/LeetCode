class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        f1,f2=0,1
        for i in range(1,n+1):
            f3=f1+f2
            f1=f2
            f2=f3
        return f1