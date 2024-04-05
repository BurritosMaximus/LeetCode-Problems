class Solution:
    def makeGood(self, s):
        stack=[s[0]] 
        for i in range(1,len(s)):
            if(stack and s[i]!=stack[-1] and s[i].lower()==stack[-1].lower()):
                stack.pop() 
            else:
                stack.append(s[i]) 
        return "".join(stack)
