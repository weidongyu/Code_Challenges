class Solution(object):
    def check(self, a, c, b, d):
        if a <= c or b <= d:
            return True
        else:
            return False

    def goThrough_iterative(self, matrix):
        if matrix == []:
            return []
        a = 0
        b = 0
        c = len(matrix) - 1
        d = len(matrix[0]) - 1
        res = []

        while a <= c and b <= d:
            for i in range(b,d+1):
                res.append(matrix[a][i])
            a += 1


            for i in range(a, c+1):
                res.append(matrix[i][d])
            d -= 1


            if a > c:
                break
            for i in range(d, b - 1, -1):
                res.append(matrix[c][i])
            c -= 1


            if b > d:
                break
            for i in range(c, a - 1, -1):
                res.append(matrix[i][b])
            b += 1

            # print a,c,'',b,d
        return res

# test cases

s = Solution()

# 1

matrix = [[1,2],[3,4]]

print s.goThrough_iterative(matrix)

matrix = [[1,2],[3,4],[5,6]]

print s.goThrough_iterative(matrix)


matrix = [[1,2]]

print s.goThrough_iterative(matrix)

matrix = [[1],[2],[3],[4]]

print s.goThrough_iterative(matrix)