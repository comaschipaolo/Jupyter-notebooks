import matplotlib.pyplot as plt
import numpy as np
import math

# costanti
msole = 2e30
mterra = 6e24
G = 6.67e-11
AU = 1.5e11
yr = 365*24*3600
vterra = 2*math.pi*AU/yr

nstep = int(1e6)
dt = 1.*yr/nstep

# posizione iniziale
x = 1.0*AU
y = 0.0
# velocità iniziale
vx = 0
vy = vterra/1.0

def accelerazione():
    r = math.sqrt(x**2 + y**2)
    modulo = G*msole/r**2

    return [-x/r*modulo, -y/r*modulo]

def passo_integrazione():
    ax, ay = accelerazione()
    global x, y, vx, vy
    x += vx*dt
    y += vy*dt
    vx += ax*dt
    vy += ay*dt

x_plot = []
y_plot = []

plt.axis("equal")
plt.axis([-1.1*AU, 1.1*AU, -1.1*AU, 1.1*AU])

for i in range(nstep):
    x_plot.append(x)
    y_plot.append(y)
    passo_integrazione()
    if i%300 == 0:
        print(i, x/AU, y/AU)

plt.plot(x_plot, y_plot)
plt.show()
