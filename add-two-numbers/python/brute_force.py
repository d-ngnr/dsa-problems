from typing import ListNode
class BruteForceApproach(object):
    def addTwoNumbers(self, listNode1: ListNode, listNode2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0
        
        while listNode1 is not None or listNode2 is not None or carry != 0:
            digit1 = listNode1.val if listNode1 is not None else 0
            digit2 = listNode2.val if listNode2 is not None else 0
            
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10
            
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next
            
            listNode1 = listNode1.next if listNode1 is not None else None
            listNode2 = listNode2.next if listNode2 is not None else None
        
        result = dummyHead.next
        dummyHead.next = None
        return result
    
def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    nums = [2,7,11,15] # declare the list of numbers
    target = 9 # declare the target sum of numbers
    print(bf.addTwoNumbers(nums, target)) # print the function return
    
if __name__ == '__main__':
    main()
    

