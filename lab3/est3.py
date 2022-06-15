import numpy as np

count = 10000

T = np.random.standard_cauchy(count)

est1 = np.sum(T) / count
est2 = np.sum(np.square(T - est1)) / count
est3 = np.sum(np.square(T - est1)) / (count - 1)

print(f'{count} & {est1} & {est2} & {est3}')