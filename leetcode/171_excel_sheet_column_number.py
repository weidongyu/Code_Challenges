class Solution(object):
    def num(self, s):
        base = 1
        n = 0
        for c in s[::-1]:
            # print c, ord(c)
            n += (ord(c) - 64) * base
            base *= 26
        return n

s = Solution()

test1 = 'AZ'
print s.num(test1)
