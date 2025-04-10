class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        max_len = 0
        for i,char in enumerate(s):
            if char == '(':
                st.append(i)
            else:
                st.pop()
                if len(st)==0:
                    st.append(i)
                else:
                    max_len = max(max_len, i-st[-1])
        return max_len
        