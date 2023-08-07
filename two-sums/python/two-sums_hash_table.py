from typing import List
class HashTableApproach(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        
        for i in range(n):
            numMap[nums[i]] = i
        
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return [] 
    
def main():
    bf = HashTableApproach() # create an instance of BruteForce
    nums = [2,7,11,15] # declare the list of numbers
    target = 9 # declare the target sum of numbers
    print(bf.twoSum(nums, target)) # print the function return
    
if __name__ == '__main__':
    main()
    

