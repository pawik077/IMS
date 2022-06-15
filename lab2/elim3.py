import matplotlib.pyplot as plt
import numpy as np

r = np.sqrt(2 / np.pi)
x = np.around(np.linspace(-r, r, 10000), decimals=3)
count = 100

f = lambda x: np.sqrt(np.square(r) - np.square(x))
g = lambda x: r * (x >= -1) * (x <= 1)

randX = np.random.uniform(-r, r, count)
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
plt.grid(), plt.legend(loc='upper left')
plt.savefig('c_plt.png')
plt.figure(2), plt.hist(acceptedX, bins=20)
plt.grid()
# plt.savefig('c_hist.eps')
print(f'Accepted: {len(acceptedX)} ({len(acceptedX) / count * 100:.2f}%)')
plt.show()