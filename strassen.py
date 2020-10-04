from utils import generateMatrix
import time
import os
import math

path = os.getcwd()+"/strassen/"
if not os.path.exists(path):
	os.mkdir(path)

def add(X, Y):
	n = len(X)
	Z = [n * [0] for x in range(0,n)]

	for i in range(0,n):
		for j in range(0,n):
			Z[i][j] = X[i][j] + Y[i][j]

	return Z

def subtract(X, Y):
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

	P1 = strassenMultiplication(A, subtract(F, H))
	P2 = strassenMultiplication(add(A,B), H)
	P3 = strassenMultiplication(add(C,D), E)
	P4 = strassenMultiplication(D, subtract(G,E))
	P5 = strassenMultiplication(add(A,D), add(E,H))
	P6 = strassenMultiplication(subtract(B,D), add(G,H))
	P7 = strassenMultiplication(subtract(A,C), add(E,F))

	P8 = add(subtract(add(P5, P4), P2), P6)
	P9 = add(P1, P2)
	P10 = add(P3, P4)
	P11 =  subtract(subtract(add(P5, P1), P3), P7)

	for i in range(0,k):
		for j in range(0, k):
			Z[i][j] = P8[i][j]
			Z[i][j+k] = P9[i][j]
			Z[k+i][j] = P10[i][j]
			Z[k+i][k+j] = P11[i][j]

	return Z

def strassen(X, Y):   
	assert type(X) == list and type(Y) == list
	assert len(X) == len(X[0]) == len(Y) == len(Y[0])

	nextPowerOfTwo = lambda n: 2 ** int(math.ceil(math.log(n, 2)))
	n = len(X)
	m = nextPowerOfTwo(n)
	XPrep = [m * [0] for j in range(m)]
	YPrep = [m * [0] for j in range(m)]

	for i in range(n):
		for j in range(n):
			XPrep[i][j] = X[i][j]
			YPrep[i][j] = Y[i][j]

	ZPrep = strassenMultiplication(XPrep, YPrep)
	Z = [n * [0] for j in range(n)]

	for i in range(n):
		for j in range(n):
			Z[i][j] = ZPrep[i][j]

	return Z


def runExperiment(n):
	timeRecord = []

	for i in range(1, n+1):
		X = generateMatrix(2**i)
		Y = generateMatrix(2**i)
		t1 = time.time()
		Z = strassenMultiplication(X, Y)
		t2 = time.time()
		timeRecord.append(t2-t1)

	with open(path + 'strassen_experiment'+str(time.time())+'.txt', 'x') as f:
		for t in timeRecord:
			f.write(str(t)+"\n")

runExperiment(8)
