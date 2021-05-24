# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:47:37 2020

@author: Aran


print(IntensityR)
print(IntensityL)

print(Total_Intensity)
print(Directionality)


"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import chain
from PIL import Image
import math


List_R = []
List_L = []

Array_to_List_R = []
Array_to_List_L = []

LogLI = []
LogRI = []

IntensityR = []
IntensityL = []




Directionality =[]
Total_Intensity = []

for i in range(0, 20):
    numbering = i + 1
    file_name1 = "4_Q45_90micW_60s  " + str(numbering)
    
    f_1 = open(file_name1 + '.csv', "r", encoding = "utf-8-sig")
    
    lines = f_1.readlines()  
    
    x_0 = []  #x
    y_0 = []  #y
    z_0 = []  #z
    
    for line in lines:
        a_1 = line.split(',')
        y_0.append(float(a_1[0]))
        x_0.append(float(a_1[1]))
        z_0.append(float(a_1[2]))
           
    array0 = np.array(z_0)
    array1 = np.array(z_0).reshape((400,1340))
    array_left = array1[ 285 : 315  , 640  : 685   ]
    array_right = array1[ 90 : 120  , 640  : 685   ]
 


    List_R = list(chain.from_iterable(array_right))    
    List_R.sort()
    List_R.reverse()
    Array_to_List_R.extend(List_R)    
    
    
    
    
    
    List_L = list(chain.from_iterable(array_left))    
    List_L.sort()
    List_L.reverse()
    Array_to_List_L.extend(List_L)    
 
    
    
    
#    print(List)

    b=[10]   
    Intensity_right = [part.sum() for part in np.split(List_R, np.cumsum(b))[:-1]]
    IntensityR.extend(Intensity_right)
    
    
    log_RI = math.log(Intensity_right[0])
    LogRI.append(log_RI)


    b=[10]   
    Intensity_left = [part.sum() for part in np.split(List_L, np.cumsum(b))[:-1]]
    IntensityL.extend(Intensity_left)

    
    log_LI = math.log(Intensity_left[0])
    LogLI.append(log_LI)

   


    total_intensity = Intensity_right[0] +  Intensity_left[0]
    directionality = (Intensity_right[0] -  Intensity_left[0])/(Intensity_right[0] +  Intensity_left[0])
     
    Total_Intensity.append(total_intensity)
    Directionality.append(directionality)
    
    
    
    f_1.close()


# print("IntensityR = ")
# print(IntensityR)
# print("IntensityL = ")
# print(IntensityL)

print("Total_Intensity = ")
print(Total_Intensity)
print("Directionality = ")
print(Directionality)

pltx = np.array(range(0,20))


fig, ax1 = plt.subplots(figsize=(10,5))

color = 'tab:red'
ax1.set_xlabel('x')
ax1.set_ylabel('Directionality')
ax1.plot(pltx, Directionality, 'or')
ax1.tick_params(axis='y')
ax1.set_ylim(-0.3, 0)
ax1.set_xticks(np.arange(0,20))

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color='tab:olive'
ax2.set_ylabel('total')  # we already handled the x-label with ax1
ax2.plot(pltx, Total_Intensity, 'oy')
ax2.tick_params(axis='y')
ax2.set_ylim(10, 40000)



fig.tight_layout()  # otherwise the right y-label is slightly clipped



plt.title("Total intensity and Directionality_sum10")

FigureName = r"./4_45_Total intensity and Directionality_sum10.png"
plt.savefig(FigureName, format="png")

  


plt.show()


