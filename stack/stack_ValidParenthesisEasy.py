'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.
Example 1:
Input: s = "()" Output: true
Example 2:
Input: s = "()[]{}" Output: true
Example 3:
Input: s = "(]" Output: false
Example 4:
Input: s = "([)]" Output: false
Example 5:
Input: s = "{[]}" Output: true
Constraints:
1 <= s.length <= 104 s consists of parentheses only '()[]{}'''


class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in s:
            if i in ['(', '{', '[']:
                queue.append(i)

            elif queue and i in [']', '}', ')']:
                braces = queue[-1] + i
                if braces in ['()', '[]', '{}']:
                    queue.pop()
                else:
                    return False
            elif not queue:
                return False
        if len(queue) == 0:
            return True
        else:
            return False


