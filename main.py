
import matplotlib.pyplot as plt

plt.grid()

xlist = []
ylist = []

debug = False
D = 8  # Digits of pi to compute
mb = 1  # Mass block B
ma = 100**(D - 1)  # Mass block A
vb_c = 0  # Velocity block B current phase
va_c = -1  # Velocity block A current phase
vb_p = 0  # Velocity block B previous phase phase
va_p = -1  # Velocity block A previous phase

n = 1  # Phase
stop = False  # Stop condition

while (stop is False):
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

    if debug is True:
        print('before ze collision')
        print('velocity b: '+str(vb_p))
        print('velocity a: '+str(va_p))

        print('after ze collision')
        print('velocity b: '+str(vb_c))
        print('velocity a: '+str(va_c))

    # Moving current velocities into previous velocity for next phase
    vb_p = vb_c
    va_p = va_c

    # Next phase
    n = n + 1

print('done after '+str(n)+' phases')

plt.plot(xlist, ylist)
plt.show()
