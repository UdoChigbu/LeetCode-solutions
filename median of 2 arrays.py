class Solution:
    def findMedianSortedArrays(self, array1: List[int], array2: List[int]) -> float:
        if len(array1)> len(array2):
            array1, array2 = array2, array1
        m = len(array1)
        n = len(array2)

        left = 0
        right = m

        
        
        while left<=right:
            i = (left+right)//2
            j = (m+n+1)//2-i
            #borders
            array1Left = float('-inf') if i == 0 else array1[i-1] 
            array1Right = float('inf') if i==m else array1[i]

            array2Left = float('-inf') if j == 0 else array2[j-1]
            array2Right = float('inf') if j==n else array2[j]

            #if perfect cut
            if array1Left<= array2Right and array2Left<=array1Right:
                if (m+n)%2 == 0:
                   return (max(array1Left, array2Left)+min(array1Right, array2Right)) / 2
                else:
                    return max(array1Left, array2Left)
            
            if array1Left > array2Right:
                right = i-1
            if array2Left > array1Right:
                left = i+1
