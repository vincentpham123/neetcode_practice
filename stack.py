class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}' : '{',
            ']' :'['
        }
        stack = []

        for c in s:
            if c not in brackets:
                stack.append(c)
                #adding in opening brackets
                continue 
            if not stack or stack[-1] != brackets[c]:
                return False 
            stack.pop()
        return not stack