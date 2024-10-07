class Solution(object):
    def isValid( s):
       
   
       
        stack = []
        opening = '({['
        closing = ')}]'
        matches = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0










    



  

