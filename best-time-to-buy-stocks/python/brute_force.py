from typing import List
class BruteForceApproach(object):
    def maximumProfit(self, prices: List) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    prices = [7,1,5,3,6,4] # declare the list of prices
    print(bf.maximumProfit(prices)) # print the function return
    
if __name__ == '__main__':
    main()
    

