from utils import generateMatrix
import time
import os

path = os.getcwd()+"/traditional/"
if not os.path.exists(path):
	os.mkdir(path)

def traditionalMatrixMultiplication(X, Y):
	n = len(X)
	
	Z = [n * [0] for x in range(0,n)]

	for i in range(0, n):
		for j in range(0, n):
			for k in range(0, n):
				Z[i][j] = Z[i][j] + (X[i][k] * Y[k][j])
	return Z


def runExperiment(n):
	timeRecord = []

	for i in range(1, n):
		X = generateMatrix(2**i)
		Y = generateMatrix(2**i)
		t1 = time.time();
		traditionalMatrixMultiplication(X, Y)
		t2 = time.time();
		timeRecord.append(t2-t1)

	with open(path +'traditional_experiment'+str(time.time())+'.txt', 'x') as f:
		for t in timeRecord:
			f.write(str(t)+"\n")


runExperiment(5)
