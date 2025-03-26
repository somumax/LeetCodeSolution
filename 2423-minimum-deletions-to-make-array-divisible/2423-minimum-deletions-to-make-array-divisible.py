class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd_ = gcd(*numsDivide)
        nums.sort()
        for i, num in enumerate(nums):
            if gcd_ % num == 0:
                return i
        return -1