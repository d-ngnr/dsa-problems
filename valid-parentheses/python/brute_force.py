from typing import List
class BruteForceApproach(object):
    def isValid(self, string: str) -> bool:
        stack = []
        for char in string:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or \
                    (char == ')' and stack[-1] != '(') or \
                    (char == '}' and stack[-1] != '{') or \
                    (char == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack

def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    string = "()[]{}" # declare string
    print(bf.isValid(string)) # print the function return
    
if __name__ == '__main__':
    main()
    

