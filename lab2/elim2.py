import matplotlib.pyplot as plt
import numpy as np

x = np.around(np.linspace(0, 1, 10000), decimals=3)
count = 100
c = 50/99

f = lambda x: 50 * (x > 0) * (x <= 0.01) + c * (x > 0.01) * (x <= 1)
g = lambda x: 50 * (x >= -1) * (x <= 1)

randX = np.random.uniform(0, 1, count)
randY = np.random.uniform(0, g(randX), count)

acceptedX = []
acceptedY = []
refusedX = []
refusedY = []

for i in range(randX.size):
	if randY[i] <= f(randX[i]):
		acceptedX.append(randX[i])
		acceptedY.append(randY[i])
	else:
		refusedX.append(randX[i])
		refusedY.append(randY[i])

plt.figure(1), plt.plot(x, f(x), label='$f(x)$'), plt.plot(x, g(x), label='$g(x)$')
plt.fill_between(x, f(x), alpha=0.3), plt.fill_between(x, g(x), alpha=0.2)
plt.plot(acceptedX, acceptedY, 'og'), plt.plot(refusedX, refusedY, 'or')
plt.grid(), plt.legend(loc='upper right')
plt.savefig('b_plt.png')
plt.figure(2), plt.hist(acceptedX, bins=20)
plt.grid()
# plt.savefig('b_hist.eps')
print(f'Accepted: {len(acceptedX)} ({len(acceptedX) / count * 100:.2f}%)')
plt.show()