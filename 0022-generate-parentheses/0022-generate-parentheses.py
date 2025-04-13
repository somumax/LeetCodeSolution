class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def findParenthesis(n,res,ans,openc,closec):
            if len(ans)==n*2:
              res.append(ans)
              return
            if openc<n:
                findParenthesis(n,res,ans+"(",openc+1,closec)
            if closec<n and closec<openc:
                findParenthesis(n,res,ans+")",openc,closec+1)
        res = []
        openc = 0
        closec = 0
        ans = ""
        findParenthesis(n,res,ans,openc,closec)
        return res
        