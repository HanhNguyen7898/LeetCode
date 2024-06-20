class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convert the integer to a string
        s = str(x)
        # Check if the string is equal to its reverse
        return s == s[::-1]
    
    
        