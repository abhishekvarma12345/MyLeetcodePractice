class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        import sys
        sys.setrecursionlimit(10**7)
        M=10**9+7
        n=len(nums)
        f=[1]*(n+1)
        invf=[1]*(n+1)
        for i in range(1,n+1):
            f[i]=(f[i-1]*i)%M
        def p(b,e):
            r=1
            while e>0:
                if e&1:
                    r=(r*b)%M
                b=(b*b)%M
                e>>=1
            return r
        invf[n]=p(f[n],M-2)
        for i in range(n-1,-1,-1):
            invf[i]=(invf[i+1]*(i+1))%M
        def C(a,b):
            if b<0 or b>a:
                return 0
            return (f[a]*((invf[b]*invf[a-b])%M))%M
        nums.sort()
        ans=0
        for i in range(n):
            for s in range(1,k+1):
                ans=(ans+nums[i]*C(i,s-1))%M
        for i in range(n):
            for s in range(1,k+1):
                ans=(ans+nums[i]*C(n-1-i,s-1))%M
        return ans%M