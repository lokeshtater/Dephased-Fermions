import numpy as np
#import matplotlib.pyplot as plt

N = 16
k = 8+8+1
nos = []
for m in range(int(N/2+1)):
    #z = np.exp(-2.0j*np.pi*m*k/(N/2))
    z = np.cos(2*np.pi*m*k/(N/2))- 1.0j*np.sin(2*np.pi*m*k/(N/2))
    #plt.plot([0, z.real], [0, z.imag], 'b-', marker='o')
    #plt.text(z.real, z.imag, f'{m}', fontsize=12, ha='right')
    #plt.text(z.real/2, z.imag/2, f'{np.abs(z)}', fontsize=12, ha='right')
    nos.append(z)

#ax = plt.gca()
#ax.set_aspect('equal', adjustable='box')
#plt.legend()
#plt.draw()

print(sum(nos)/N)