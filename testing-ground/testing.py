

class BruteForceApproach(object):
    def countSetBits(self, number: int) -> int:
        count = 0
        while (number):
            number = number & (number - 1)
            count += 1
        
        return count
    
def main():
    bf = BruteForceApproach() # create an instance of BruteForce
    number = 9
    print(bf.countSetBits(number))
    
if __name__ == '__main__':
    main()