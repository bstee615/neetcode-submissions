class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CLOSING = ']})'
        OPENING = '[{('
        for c in s:
            if (i := CLOSING.find(c)) != -1:
                if len(stack) == 0:
                    return False
                if stack[-1] == OPENING[i]:
                    # valid
                    print("valid", stack, c)
                    stack.pop(-1)
                else:
                    # invalid
                    return False
            elif c in OPENING:
                stack.append(c)
                print("add", c, stack)
        print("end", stack)
        return len(stack) == 0
