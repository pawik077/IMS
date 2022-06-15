import sys
import math
import matplotlib.pyplot as plt
def sawToothGen(n, X0, z):
	X = [X0]
	for Xn in range(n):
		X.append(z * X[-1] - math.floor(z * X[-1]))
	return X
def genPlots(N, X0, Z, showPlots):
	X=sawToothGen(N, X0, Z)
	plt.figure(1), plt.hist(X, bins=100)
	plt.savefig(f'N={N}-X0={X0}-Z={Z}-hist.eps')
	plt.figure(2), plt.plot(X, 'o')
	plt.savefig(f'N={N}-X0={X0}-Z={Z}-plot.eps')
	if showPlots:
		plt.show()
def genValues(N, X0, Z, printValues):
	X=sawToothGen(N, X0, Z)
	if printValues:
		for i in range(N):
			print(X[i])
	with open(f'N={N}-X0={X0}-Z={Z}-values.csv', 'w') as f:
		for i in range(N):
			f.write(f'{i}, {X[i]}\n')

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('No arguments given!!')
	elif sys.argv[1] == 'plots':
		try:
			N = int(sys.argv[2])
			X0 = float(sys.argv[3])
			Z = int(sys.argv[4])
			showPlots = bool(sys.argv[5]) if len(sys.argv) >= 6 else False
			genPlots(N, X0, Z, showPlots)
		except IndexError:
			print('Insufficient arguments')
		except ValueError:
			print('Incorrect arguments!!')
	elif sys.argv[1] == 'values':
		try:
			N = int(sys.argv[2])
			X0 = float(sys.argv[3])
			Z = int(sys.argv[4])
			printValues = bool(sys.argv[5]) if len(sys.argv) >= 6 else False
			genValues(N, X0, Z, printValues)
		except IndexError:
			print('Insufficient arguments')
		except ValueError:
			print('Incorrect arguments!!')
	else:
		print('Unknown arguments!!')
