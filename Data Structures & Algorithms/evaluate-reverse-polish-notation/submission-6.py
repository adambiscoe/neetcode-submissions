class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                i = int(s)
                return i
            except ValueError:
                return -300
        currVal = int(tokens[0])
        stack = []
        for i in range(len(tokens)):
            val = is_number(tokens[i])
            if not val == -300:
                stack.append(val)
            else:
                if tokens[i] == "+":
                    currVal = stack.pop() + stack.pop()
                    stack.append(currVal)
                elif tokens[i] == "-":
                    currVal = stack.pop()
                    currVal = stack.pop() - currVal
                    stack.append(currVal)
                elif tokens[i] == "*":
                    currVal = stack.pop() * stack.pop()
                    stack.append(currVal)
                elif tokens[i] == "/":
                    second = stack.pop()
                    currVal = int(stack.pop() / second)
                    stack.append(currVal)
                    
        return currVal



        