import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpldatacursor import datacursor

file_name1 = "4_Q45_90micW_60s  5"

plt.figure(figsize=(5, 10))

f_1 = open(file_name1 + '.csv', "r", encoding = "utf-8")

lines = f_1.readlines() 
#=[ , , , ]
x_0 = []  #x
y_0 = []  #y
z_0 = []  #z


for line in lines:

    a_1 = line.split(',')

    y_0.append(float(a_1[0]))
    x_0.append(float(a_1[1]))
    z_0.append(float(a_1[2]))


array1 = np.array(z_0)
array = np.array(z_0).reshape((400,1340))

f_1.close()

x = x_0
y = y_0
z = z_0



#fig, ax = plt.subplots()
#ax.imshow(array, interpolation='none', extent=[0, 1.5*np.pi, 0, np.pi])


plt.scatter(x, y, c=z, marker = 's', s=105, cmap=plt.cm.YlOrRd, vmin = 10, vmax = 2000, alpha=1)
plt.colorbar(label='intensity')
plt.xlabel('x')
plt.xlim(600,700)
plt.ylabel('y')
plt.ylim(0, 390)
plt.title(file_name1)
plt.tight_layout()
plt.show()
