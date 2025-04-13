class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(remtarget,combo,idx):
            if remtarget == 0:
                res.append(list(combo))
                return
            if remtarget<0:
                return
            for i in range(idx, len(candidates)):
                combo.append(candidates[i])
                backtracking(remtarget-candidates[i],combo,i)
                combo.pop()

        res = []
        backtracking(target, [],0)
        return res
        