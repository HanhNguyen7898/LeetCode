class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        
        #initialize the result
        result = 0
        
        #length of the input string
        n = len(s)
        
        # iterate over the string
        for i in range(n): 
            #if the current value is less than the next value, subtract the current value
            if i < n - 1 and roman_to_integer[s[i]] < roman_to_integer[s[i+1]]: 
                result -= roman_to_integer[s[i]]
            else: 
                result += roman_to_integer[s[i]]
                
        return result
        
    
        