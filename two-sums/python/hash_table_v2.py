from typing import List
class HashTableApproach(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # create a map to hold the numbers
        n = len(nums) # get the length of the list
        
        for i in range(n): # iterate up to the lenght of the list
            numMap[nums[i]] = i # add the numbers to the map e.g. {2:0, 7:1, 11:2, 15:3}
        
        for i in range(n): # iterate up to the lenght of the list
            complement = target - nums[i] # calculate the complement by substracting the numbers from the target value
            if complement in numMap: # check if the complement is in the map
                return [i, numMap[complement]] # return the indices of the iterator and the complement
            numMap[nums[i]] = i # if complement is not in the map then add it to the map
        return [] # return an empty set if the nothing satisfies the condition
    
def main():
    bf = HashTableApproach() # create an instance of HashTableApproach
    nums = [2,7,11,15] # declare the list of numbers
    target = 9 # declare the target sum of numbers
    print(bf.twoSum(nums, target)) # print the function return
    
if __name__ == '__main__':
    main()
    

