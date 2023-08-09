from typing import List
class BruteForceApproach(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) # get the length of the list
        for i in range(n - 1): # iterate the elements in the array starting from index 0 to the 2nd to the last element
            for j in range(i + 1, n): # iterate the elements from the next element to the last element
                if nums[i] + nums[j] == target: # add the numbers and check if it equals the target
                    return [i,j] # return the indices if the sum of numbers matches the target
        return [] # return an empty set if the nothing satisfies the condition
    
def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    nums = [2,7,11,15] # declare the list of numbers
    target = 9 # declare the target sum of numbers
    print(bf.twoSum(nums, target)) # print the function return
    
if __name__ == '__main__':
    main()
    

