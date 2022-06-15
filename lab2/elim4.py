import matplotlib.pyplot as plt
import numpy as np

x = np.around(np.linspace(-5, 5, 100000), decimals=3)
count = 100
c = 1 / np.sqrt(2 * np.pi)

f = lambda x: (1 / np.sqrt(2 * np.pi)) * np.exp(-np.square(x) / 2)
g = lambda x: c * (x >= -4) * (x <= 4)

randX = np.random.uniform(-4, 4, count)
randY = np.random.uniform(0, 1, count) * g(randX)

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
plt.grid(), plt.legend(loc='upper left')
plt.savefig('d_plt.png')
plt.figure(2), plt.hist(acceptedX, bins=20)
plt.grid()
# plt.savefig('d_hist.eps')
print(f'Accepted: {len(acceptedX)} ({len(acceptedX) / count * 100:.2f}%)')
plt.show()