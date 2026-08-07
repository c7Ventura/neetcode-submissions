class Solution:
    # only given valid array of strings
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        output = 0
        for i in range(len(tokens)):
            # if current item is not a number, it is operator.
            if tokens[i] in "+-*/":
                # num operator num forms proper int evaluation
                right = int(nums.pop())
                left = int(nums.pop())
                if tokens[i] == "+":
                    output = left + right
                elif tokens[i] == "-":
                    output = left - right
                elif tokens[i] == "*":
                    output = left * right
                elif tokens[i] == "/":
                    output = int(left / right)
                nums.append(output)
                
            # current item IS number, need second 
            else:
                nums.append(tokens[i])

        # only one element should be left on stack. Pop final result from stack
        return int(nums.pop())
            