import matplotlib.pyplot as plt
import numpy as np
import math

# funzione di esempio
f = lambda x: math.sin(x)/x-0.5

# valori per grafico
x = np.linspace(0, 3, 100)
y = list(map(f, x))

# inizializzazione estremi
xmin = 0.1
xmax = 3
assert f(xmin)*f(xmax) < 0

# precisione dello zero
delta = 0.01

# inizializzazione grafico
plt.plot(x,y)
plt.scatter(xmin, 0, color = "r")
plt.scatter(xmax, 0, color = "b")
plt.pause(1)

# ciclo di bisezione
while xmax - xmin > delta:

    xmed = (xmin + xmax)/2

    # visualizzazione grafico
    plt.clf()
    plt.plot(x,y)
    plt.scatter(xmin, 0, color = "r")
    plt.scatter(xmax, 0, color = "b")
    plt.scatter(xmed,0, color = "g")
    plt.pause(1)

    # restrizione intervallo
    if f(xmed)*f(xmin) > 0:
        xmin = xmed
    else:
        xmax = xmed

plt.show()