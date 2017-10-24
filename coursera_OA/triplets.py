class Solution(object):
    def trip(self, d,t):
        self.res = 0
        d.sort()
        l = len(d)
        for i in range(l - 1):
            j = i+1
            k = l - 1
            while j<k:
                s = d[i] + d[j] + d[k]
                if s>t:
                    k -= 1
                else:
                    self.res += (k-j)
                    j+=1
        return self.res
