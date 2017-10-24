import math
class Solution(object):
    def romanToInt(self):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0

        def nCr(n, r):
            f = math.factorial
            return f(n) / f(r) / f(n - r)
        def nAr(n, r):
            f = math.factorial
            return f(n) / f(n - r)

        def count(N, L, K):
            dp = [0] * (N+1)
            dp[K+1] = nAr(K+1,K+1)%1000000007
            for i in range(K+2, N+1):
                base = nAr(i,K+1)*((i-K)**(L-K-1))%1000000007
                for j in range(K+1,i):
                    base -= nCr(i,j)*dp[j]
                dp[i] = base%1000000007
            return dp[N]
        def includeAll(N, numStr):

            for i in range(1, N + 1):
                if str(i) not in numStr:
                    return False
            # print 'include', numStr
            return True

        from itertools import product
        a = '123'
        b = 3
        print [''.join(x) for x in product(a, repeat=b)]

        def helper(N, L, K, cur, path):
            # print path, cur
            if cur == L + 1:
                if includeAll(N, path):
                    self.res += 1
                return
            for i in range(1, N + 1):
                if str(i) not in path[-K:]:
                    helper(N, L, K, cur + 1, path + str(i))
        helper(4, 8, 2, 1, '')
        print self.res

        print 'count', count(7,10,5)
        return self.res


m = Solution()
m.romanToInt()