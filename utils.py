import random

def printMatrix(matrix):
	for line in matrix:
		print(line)

def generateMatrix(n):
	matrix = []

	for i in range(0,n):
		matrix.append(random.choices(range(0,100), 100*[1], k= n))

	return matrix