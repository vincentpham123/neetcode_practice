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
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # how can i use a stack to solve this
        stack = []

        # what will be in stack 
        # maybe i put the index of each temperature

        # how do i keep track of the amount of days 
        # i can subtract the index to get the amount of days 
        output = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                #if stack has a number and its greater, i want to pop and adjust the index in output
                current_day = stack.pop()
                #current_day will be an index 
                output[current_day] = index - current_day 
                # that should update the current number 

            stack.append(index)
        return output
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    def generateParenthesis(self, n: int) -> List[str]:
            stack = []
            res = []

            def backtrack(openN, closedN):
                if openN == closedN == n:
                    res.append("".join(stack))
                    return

                if openN < n:
                    stack.append("(")
                    backtrack(openN + 1, closedN)
                    stack.pop()
                if closedN < openN:
                    stack.append(")")
                    backtrack(openN, closedN + 1)
                    stack.pop()

            backtrack(0, 0)
            return res             
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