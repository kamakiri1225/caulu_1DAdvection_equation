import numpy as np
import matplotlib.pyplot as plt
 
nx = 101
dx = 2 / (nx-1)
nt = 25
c = 1
alpha = 1.0
dt = alpha * (dx/c) 
 
x = np.linspace(0,2,nx)
 
un = []
u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2
 
 
for n in range(nt): 
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
 
u_final = u.copy()
 
u_initial  = np.ones(nx)
u_initial[int(.5 / dx):int(1 / dx + 1)] = 2
 
plt.plot(x,u_initial,label = 'initial')
plt.plot(x,u_final, label = 'final')
plt.legend()
# plt.show()
plt.savefig('figure01.jpg')