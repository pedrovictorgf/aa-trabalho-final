import os
import re
import numpy
import matplotlib.pyplot as plt


strassen_path = os.getcwd()+"/strassen/"
traditional_path = os.getcwd()+"/traditional/"

strassen_entries = os.listdir(strassen_path)
traditional_entries = os.listdir(traditional_path)

strassen_stats = []
traditional_stats = []

for entry in strassen_entries:
	with open(strassen_path+entry, 'r') as file:
		aux = []
		for line in file:
			aux.append(float(re.sub('\n', '', line)))
		strassen_stats.append(aux)

for entry in traditional_entries:
	with open(traditional_path+entry, 'r') as file:
		aux = []
		for line in file:
			aux.append(float(re.sub('\n', '', line)))
		traditional_stats.append(aux)

n = len(strassen_stats[0])

strassen_mean = [numpy.mean(x) for x in zip(*strassen_stats)]
traditional_mean = [numpy.mean(x) for x in zip(*traditional_stats)]
strassen_std = [numpy.std(x) for x in zip(*strassen_stats)]
traditional_std = [numpy.std(x) for x in zip(*traditional_stats)]

x = [2**x for x in range(1,n+1)]

plt.xlabel('size of n')
plt.ylabel('time (s)')
plt.plot(x, strassen_mean, color='red', label='strassen mean')
plt.plot(x, traditional_mean, color='blue', label='traditional mean')
plt.legend()
plt.savefig('means.png')

plt.clf()

plt.xlabel('size of n')
plt.ylabel('time (s)')
plt.plot(x, strassen_std, color = 'green', label='strassen std')
plt.plot(x, traditional_std, color = 'yellow', label='traditional std')
plt.legend()
plt.savefig('std.png')