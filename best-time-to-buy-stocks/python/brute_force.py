from typing import List
class BruteForceApproach(object):
    def isValid(self, string: str) -> bool:
        stack = [] # create an empty list to store the opening brackers
        for char in string: # loop through the characters in the string
            if char in '([{': # check if the character is an open bracket
                stack.append(char) # if it is an open bracket then push it onto the stack
            else: # if a character is a closing bracket
                if not stack or \
                    (char == ')' and stack[-1] != '(') or \
                    (char == '}' and stack[-1] != '{') or \
                    (char == ']' and stack[-1] != '['):
                    return False # the string is not valid at this point so return False
                stack.pop() # else, remove the opening bracket from the stack
        return not stack # if the stack is empty then all of the opening brackets have been
                         # matched with a matching closing bracket (string is valid) so return True
                         # otherwise, return False

def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    string = "()[]{}" # declare string
    print(bf.isValid(string)) # print the function return
    
if __name__ == '__main__':
    main()
    

