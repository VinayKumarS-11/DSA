class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            for j in range(i+1,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(m):
            matrix[i].reverse()

obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print("Original Matrix:")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()

obj.rotate(matrix)

print("Rotated Matrix:")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()