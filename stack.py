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
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        Map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False 
            stack.pop()
        return not stack
    
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:

            if i == '+' and len(stack)>=2:
                stack.append(stack[-1] + stack[-2])
                continue
            if i == 'D' and len(stack)>=1:
                stack.append(stack[-1]*2)
                continue
            if i == 'C' and len(stack)>=1:
                stack.pop()
                continue
            stack.append(int(i))
        
        return sum(stack)
    
class MyStack:

    def __init__(self):
        self.stack = collections.deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self) -> int:
        for i in range(len(self.stack) - 1):
            self.push(self.stack.popleft())
        res = self.stack[0]
        self.push(self.stack.popleft())
        return res

    def empty(self) -> bool:
        
        return len(self.stack) == 0
    def removeStars(self, s: str) -> str:
        stack = []


        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    class Solution:
def generateParenthesis(self, n: int) -> List[str]:
        
    stack =[]
    res = []

    def backtrack(openN, closeN):

        # we know that there will be equal open and close 
        if openN == closeN == n:
            res.append(''.join(stack))
            return 
        

        # i start by adding the open parenthesis 

        if openN < n:
            stack.append('(')
            backtrack(openN+1, closeN)
            stack.pop()
            # this is the backtrack
        if closeN < openN:
            stack.append(')')
            backtrack(openN, closeN+1)
            stack.pop()
    
    backtrack(0,0)
    return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # the trick to this problem is to determine the time that each 

        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort()

        stack = []
        # stack will be used to keep track the the most recently added time
        for i in range(len(pairs)-1, -1, -1):
            # going reverse from position
            position, speed = pairs[i]

            time = (target-position)/speed

            stack.append(time)

            # how do i know if i have a fleet, when the speed of a car is slower 
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)