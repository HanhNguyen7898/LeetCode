class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        #Take the first string as the initial prefix
        prefix = strs[0]
        
        #Compare the prefix with each string in the list
        for string in strs[1:]: 
            #Reduce the prefix until it matches the beginning of the current string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix: 
                    return ""
                
        return prefix