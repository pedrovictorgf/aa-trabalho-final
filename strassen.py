from utils import generateMatrix
import time
import os

def addMatrices(X, Y):
	n = len(X)
	Z = [n * [0] for x in range(0,n)]

	for i in range(0,n):
		for j in range(0,n):
			Z[i][j] = X[i][j] + Y[i][j]

	return Z

def subMatrices(X, Y):
	n = len(X)
	Z = [n * [0] for x in range(0,n)]

	for i in range(0,n):
		for j in range(0,n):
			Z[i][j] = X[i][j] - Y[i][j]
	return Z 


def strassenMultiplication(X, Y):
	n = len(X)
	Z = [n * [0] for x in range(0, n)]

	if n == 1:	
		Z[0][0] = X[0][0] * Y[0][0]
		return Z

	k = int(n/2)

	A = [k * [0] for x in range(0,k)]
	B = [k * [0] for x in range(0,k)]
	C = [k * [0] for x in range(0,k)]
	D = [k * [0] for x in range(0,k)]
	E = [k * [0] for x in range(0,k)]
	F = [k * [0] for x in range(0,k)]
	G = [k * [0] for x in range(0,k)]
	H = [k * [0] for x in range(0,k)]

	for i in range(0, k):
		for j in range(0, k):
			A[i][j] = X[i][j]
			B[i][j] = X[i][k+j]
			C[i][j] = X[k+i][j]
			D[i][j] = X[k+i][k+j]
			E[i][j] = Y[i][j]
			F[i][j] = Y[i][k+j]
			G[i][j] = Y[k+i][j]
			H[i][j] = Y[k+i][k+j]

	P1 = strassenMultiplication(A, subMatrices(F, H))
	P2 = strassenMultiplication(addMatrices(A,B), H)
	P3 = strassenMultiplication(addMatrices(C,D), E)
	P4 = strassenMultiplication(D, subMatrices(G,E))
	P5 = strassenMultiplication(addMatrices(A,D), addMatrices(E,H))
	P6 = strassenMultiplication(subMatrices(B,D), addMatrices(G,H))
	P7 = strassenMultiplication(subMatrices(A,C), addMatrices(E,F))

	P8 = addMatrices(subMatrices(addMatrices(P5, P4), P2), P6)
	P9 = addMatrices(P1, P2)
	P10 = addMatrices(P3, P4)
	P11 =  subMatrices(subMatrices(addMatrices(P5, P1), P3), P7)

	for i in range(0,k):
		for j in range(0, k):
			Z[i][j] = P8[i][j]
			Z[i][j+k] = P9[i][j]
			Z[k+i][j] = P10[i][j]
			Z[k+i][k+j] = P11[i][j]

	return Z

def runExperiment(n):
	timeRecord = []

	for i in range(1, n):
		X = generateMatrix(2**n)
		Y = generateMatrix(2**n)
		t1 = time.time();
		Z = strassenMultiplication(X, Y)
		t2 = time.time();
		timeRecord.append(t2-t1)

	with open(os.getcwd() + '/strassen/strassen_experiment'+str(time.time())+'.txt', 'x') as f:
		for t in timeRecord:
			f.write(str(t)+"\n")


runExperiment(5)