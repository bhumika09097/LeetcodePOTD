#Brute Force Approach (TLE)
class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)
    

    def getProduct(self, k: int) -> int:
        product = 1
        n = len(self.nums)
        for i in range(n-k,n):
            product *= self.nums[i]

        return product



