#YASHODEEP PAWAR USERID:2470

def countSpecialElements(matrix):
    nRows = len(matrix)
    print(nRows)
    nCount = 0

    for row in matrix:
        for indexCol, element in enumerate(row):

            if element == min(row) or element == max(row):
                if row.count(element) > 1:
                    return -1
                nCount = nCount + 1

            else:
                listColumn = []

                for indexRow in range(0, nRows):
                    listColumn.append(matrix[indexRow][indexCol])

                if element == min(listColumn) or element == max(listColumn):
                    if listColumn.count(element) > 1:
                        return -1
                    nCount = nCount + 1

    return nCount


# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# Initialize matrix
def slicing(a, step):
    return [a[i::step] for i in range(step)]


# print(slicing(a,3))

matrixx = []
print("Enter the entries rowwise:")

# For user input
a = []
for i in range(3):  # A for loop for row entries
    # a =[]
    for j in range(3):  # A for loop for column entries
        a.append(int(input()))
    matrixx.append(a)
mat = slicing(a, 3)
print(mat)
# print(slicing(a,3))

if __name__ == '__main__':
    nCount = countSpecialElements(mat)
    print(nCount)

# A basic code for matrix input from user


'''
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrixx[i][j], end = " ")
   # print()
'''

