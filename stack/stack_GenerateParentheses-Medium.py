''' Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3 Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1 Output: ["()"]

Constraints:

1 <= n <= 8'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def recursiveFunc(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append('(')
                recursiveFunc(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                recursiveFunc(openN, closeN + 1)
                stack.pop()

        recursiveFunc(0, 0)
        return res