from typing import List
class BruteForceApproach(object):
    def maximumProfit(self, prices: List) -> int: 
        left = 0 # start index of the price slider from the left
        right = 1 # second index in the price slider from the left
        max_profit = 0 # initial value of the maximum profit
        while right < len(prices): # loop until the right value is reached
            currentProfit = prices[right] - prices[left] # calculate the current profit by subtracting the left price from the right price
            if prices[left] < prices[right]: # check if the left price is less than the right price
                max_profit = max(currentProfit,max_profit) # if it is then we calculate the profit
            else: # if the left price is greater than the right price
                left = right # assign the right index value to the left index to move the price slider to the right
            right += 1 # increment the right index
        return max_profit # return the max profit after the slider reaches the last index
        
def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    prices = [7,1,5,3,6,4] # declare the list of prices
    print(bf.maximumProfit(prices)) # print the function return
    
if __name__ == '__main__':
    main()
    

