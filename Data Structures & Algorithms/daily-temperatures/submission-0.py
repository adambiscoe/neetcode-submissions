class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                item = stack.pop()
                ret[item[1]] = i - item[1]
            stack.append((temperatures[i], i))
        return ret


        

        