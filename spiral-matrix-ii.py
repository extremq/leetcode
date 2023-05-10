class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for i in range(n)]

        start_size = n
        start_number = 1
        start_offset = 0
        while start_size > 0:
            start_number = self.generate_square(start_number, matrix, start_size, start_offset)
            start_size -= 2
            start_offset += 1
        
        return matrix

    def generate_square(self, start, matrix, n, offset):
        counter = start
        for i in range(n):
            matrix[0 + offset][i  + offset] = counter
            counter += 1
        
        for i in range(1, n):
            matrix[i  + offset ][n - 1 + offset] = counter
            counter += 1
        
        for i in range(1, n):
            matrix[n - 1 + offset][n - i - 1 + offset] = counter
            counter += 1
        
        for i in range(1, n - 1):
            matrix[n - i - 1 + offset][0 + offset] = counter
            counter += 1
        
        return counter
    
    def print_matrix(self, matrix):
        for row in matrix:
            print(row)

s = Solution()
s.print_matrix(s.generateMatrix(3))