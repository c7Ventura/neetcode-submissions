class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isValP = True
        isValB = True
        isValS = True
        for i in s:
            if i == "(":
                stack.append("(")
                isValP = False
            elif i == "[":
                stack.append("[")
                isValS = False
            elif i == "{":
                stack.append("{")
                isValB = False
            
            elif  i == ")":
                # check for corresponding closing bracket.
                    if stack and stack.pop() == "(":
                        isValP = True
                    else: return False
            elif i == "]":
                 if stack and stack.pop() == "[":
                    isValS = True
                 else: return False
            elif  i == "}":
                 if stack and stack.pop() == "{":
                    isValB = True
                 else: return False

        # if there is no remaining items on the stack, all accounted for. 
        if stack == []:
            return True
        else: return False
        # if it passes all other cases, return True
        if isValP and isValB and isValS: return True
        else: return False
            