import pyfmm
import matplotlib.pyplot as plt
import numpy as np

# Define a boundary resembling a circle
n = 300
my_mesh = np.zeros((n, n), dtype=np.bool)
xx = np.array(100 + 50 * np.cos(np.linspace(0, 2 * np.pi, 100)), dtype=np.int)
yy = np.array(100 + 50 * np.sin(np.linspace(0, 2 * np.pi, 100)), dtype=np.int)
my_mesh[xx, yy] = True

# Compute solution
solution_n1 = pyfmm.march(my_mesh, batch_size=1)
solution_n20 = pyfmm.march(my_mesh, batch_size=20)
solution_n100 = pyfmm.march(my_mesh, batch_size=100)
solution_ninf = pyfmm.march(my_mesh, batch_size=np.inf)

plt.subplot(2,2,1)
plt.title('n = 1')
plt.imshow(solution_n1[0], interpolation='None')
plt.colorbar()

plt.subplot(2,2,2)
plt.title('n = 20')
plt.imshow(solution_n20[0], interpolation='None')
plt.colorbar()

plt.subplot(2,2,3)
plt.title('n = 100')
plt.imshow(solution_n100[0], interpolation='None')
plt.colorbar()

plt.subplot(2,2,4)
plt.title('n = inf')
plt.imshow(solution_ninf[0], interpolation='None')
plt.colorbar()
plt.show()
