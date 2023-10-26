class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # For this we are going to be doing backtracking recursion
        # Variables it is going to use is 'openN' and 'closeN'
        # The basecase to stop the recursion function:
        #   When openN == closeN == N, then we can return the result since the parentheses cap has been met.
        
        stack = []
        res = []

        def backtracking(openN, closeN):

            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN + 1)
                stack.pop()
            
            if openN < n:
                stack.append("(")
                backtracking(openN  + 1, closeN)
                stack.pop()

        backtracking(0,0)

        return res
        

        