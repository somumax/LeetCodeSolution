class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(nums, perm, res):
            if not nums:
                res.append(perm)
                return
            for i in range(len(nums)):
                newnums = nums[:i]+nums[i+1:]
                permutation(newnums,perm+[nums[i]],res)
        res = []
        permutation(nums, [],res)
        return res