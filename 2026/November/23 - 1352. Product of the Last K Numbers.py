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

# Optimal Approach
class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        n = len(self.nums)
        if num == 0:
            self.nums = [] 
        else:
            if n != 0:
                self.nums.append(num * self.nums[n-1])
            else:
                self.nums.append(num)

    def getProduct(self, k: int) -> int:
        product = 1
        n = len(self.nums)
        if n < k:
            return 0
        elif n == k:
            return self.nums[n-1]
        else:
            return (self.nums[n-1] // self.nums[n-k-1])




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)



