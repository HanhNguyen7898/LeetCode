class Solution:
    def isValid(self, s: str) -> bool:
        # Matching pairs
        matching = {')':'(', ']':'[', '}':'{'}
        
        #Stack to keep track of opening parentheses
        stack = []
        
        for char in s:
            if char in matching.values():
                #If the character is one of '(', '[', or '{', push it onto the stack
                stack.append(char)
            elif char in matching.keys():
                # If the character is one of ')', ']', or '}', check if stack is empty or the top of the stack does not match
                if stack == [] or matching[char]!= stack.pop():
                    return False
            else:
                #If the character is not a parentheses, ignore it
                continue
                
        #If the stack is empty, all opening parentheses had matching closing ones
        return stack == []
    

        