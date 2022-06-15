import sys
import matplotlib.pyplot as plt
import numpy as np
def randomGen(N, X0, k, m, c):
	X = np.zeros(1)
	X[0] = X0
	for i in range(1, N):
		if(i <= k):	A = np.arange(i) + 1
		else: A = np.append(A, 0)
		X = np.append(X, np.mod((A * np.flip(X)).sum() + c, m))
	return X
def genPlots(N, X0, k, m, c, showPlots):
	X=randomGen(N, X0, k, m, c)
	plt.figure(1), plt.hist(X, bins=100)
	plt.savefig(f'N={N}-X0={X0}-k={k}-m={m}-c={c}-hist.eps')
	plt.figure(2), plt.plot(X, 'o')
	plt.savefig(f'N={N}-X0={X0}-k={k}-m={m}-c={c}-plot.eps')
	if showPlots:
		plt.show()
def genValues(N, X0, k, m, c, printValues):
	X=randomGen(N, X0, k, m, c)
	if printValues:
		for i in range(len(X)):
			print(X[i])
	with open(f'N={N}-X0={X0}-k={k}-m={m}-c={c}-values.csv', 'w') as f:
		for i in range(len(X)):
			f.write(f'{i}, {X[i]}\n')

def main():
	if len(sys.argv) == 1:
		print('No arguments given!!')
	elif sys.argv[1] == 'plots':
		try:
			N = int(sys.argv[2])
			X0 = float(sys.argv[3])
			k = int(sys.argv[4])
			m = float(sys.argv[5])
			c = float(sys.argv[6])
			showPlots = bool(sys.argv[7]) if len(sys.argv) >= 8 else False
			genPlots(N, X0, k, m, c, showPlots)
		except IndexError:
			print('Insufficient arguments')
		except ValueError:
			print('Incorrect arguments!!')
	elif sys.argv[1] == 'values':
		try:
			N = int(sys.argv[2])
			X0 = float(sys.argv[3])
			k = int(sys.argv[4])
			m = float(sys.argv[5])
			c = float(sys.argv[6])
			printValues = bool(sys.argv[7]) if len(sys.argv) >= 8 else False
			genValues(N, X0, k, m, c, printValues)
		except IndexError:
			print('Insufficient arguments')
		except ValueError:
			print('Incorrect arguments!!')
	else:
		print('Unknown arguments!!')



if __name__ == '__main__':
	main()
