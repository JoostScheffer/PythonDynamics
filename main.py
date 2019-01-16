import numpy
import matplotlib.pyplot as plt

plt.grid()

xlist = []
ylist = []

debug = False
mb = 1
d = 8
ma = 100**(d-1)
vb_c = 0
va_c = -1
va_p = -1
vb_p = 0
n = 1
stop = False

while (stop == False):
    
    if debug == True:
        print('before ze collision')
        print('velocity b: '+str(vb_p))
        print('velocity a: '+str(va_p))

    if debug == True:
        print('after ze collision')
        print('velocity b: '+str(vb_c))
        print('velocity a: '+str(va_c))
    
    xlist.append(va_c)
    ylist.append(vb_c)

    if (vb_c < 0):
        vb_c = vb_c * -1

    else:
        vb_c = (2*va_p * ma/mb + (1 - ma/mb)*vb_p) / (1 + ma/mb)
        va_c = (2*vb_p * mb/ma + (1-mb/ma) * va_p) / (1+mb/ma)

    if (vb_c >= 0) and (va_c > 0) and (vb_c < va_c):
        stop = True
        break

    vb_p = vb_c
    va_p = va_c

    n = n + 1

print('done after '+str(n)+' phases')

plt.plot(xlist, ylist)
plt.show()
        
    
        
    
