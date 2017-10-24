class Solution(object):
    def preTextSuf(self,pre,suf,ori):
        """
        :type s: str
        :rtype: str
        """
        lo = len(ori)
        lp = len(pre)
        ls = len(suf)
        preCache  = [0] * lo
        sufCache = [0] * lo

        for i in range(lo):
            # check pre
            lc = 0
            while lc <= i and lc <= lp - 1 and ori[i - lc] == pre[lp - 1 - lc]:
                preCache[i - lc] = lc + 1
                lc += 1
        for i in range(lo, -1, -1):
            # check suf
            lc = 0
            while i+lc <= lo - 1 and lc <= ls - 1 and ori[i+lc] == suf[lc]:
                sufCache[i+lc] = lc + 1
                lc += 1
        print preCache,sufCache
        maxPreInd = 0
        maxScore = 0
        res = ''
        # for i in range(lo):
        #     if sufCache[i] + preCache[maxPreInd] > maxScore:
        #
        # return preCache,sufCache
m = Solution()
m.preTextSuf('bruaaaa','aaathenious','aaaaaing')