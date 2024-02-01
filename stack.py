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
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for c in tokens:
            if c =='+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[0]
                
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        # now i need to keep track of the current min in the stack 
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]