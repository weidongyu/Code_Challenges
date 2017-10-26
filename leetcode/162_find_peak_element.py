class Solution(object):
    def findPeak(self, nums):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi)/2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        return lo

s = Solution()

# test cases

nums = [1]

print s.findPeak(nums)

nums = [1,2]

print s.findPeak(nums)

nums = [1,2,1]

print s.findPeak(nums)
