class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
    

        if n==1:
            return True
        elif n%2==0:
            return self.isPowerOfTwo(n/2)
        else:
            return False
solution = Solution()
#print(solution.isPowerOfTwo(1))  # True
print(solution.isPowerOfTwo(16))  # True
#print(solution.isPowerOfTwo(3))  # False