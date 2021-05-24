import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

for i in range(0, 20):
    numbering = i + 1
    file_name1 = "4_Q45_90micW_60s  " + str(numbering)
    
    f_1 = open(file_name1 + '.csv', "r", encoding = "utf8")
    
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
#    array_up = array1[ 295 : 320  , 640 + i  : 680 + i ]
#    array_dw = array1[ 105 : 130  , 640 + i : 680 + i ]
#    array_up = array1[ 285 : 315  , 645 +i : 660 +2*i  ]
#    array_dw = array1[ 90 : 120  , 645 +i : 660 +2*i  ]
    array_up = array1[ 285 : 315  , 640  : 685   ]
    array_dw = array1[ 90 : 120  , 640  : 685   ]
     
    
    up_max = np.argmax(array_up)
    dw_max = np.argmax(array_dw)
    
#    up.append((up_max)%101)
#    dw.append((dw_max)%101)
    
    fig = plt.figure()
    rows = 1
    cols = 2 
    ax1 = fig.add_subplot(rows, cols, 1)
    ax1.imshow(array_up, cmap='hot')
    ax1.set_title('up'+ str(numbering))

     
    ax2 = fig.add_subplot(rows, cols, 2)
    ax2.imshow(array_dw, cmap='hot')
    ax2.set_title('dw'+ str(numbering))
    FigureName = r"./4_45_NW end" + str(numbering)+ ".png"
    plt.savefig(FigureName, format="png")

     
    plt.show()

    
    f_1.close()

