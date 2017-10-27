class Solution(object):
    def find(self, matrix, target):
        if matrix == []:
            return False

        curC = len(matrix[0]) - 1
        curR = 0

        while curR < len(matrix) and curC >= 0:
            curNum = matrix[curR][curC]
            if curNum > target:
                curC -= 1
            elif curNum < target:
                curR += 1
            elif target == curNum:
                return True
        return False


s = Solution()
# test cases

# test 1
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

print s.find(matrix, 0)


