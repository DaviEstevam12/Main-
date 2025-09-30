import numpy as np
import matplotlib.pyplot as plt

# tempo
t = np.linspace(-1,4,400)
# posição
x = t**3 - 6*t**2 + 9*t
# velocidade
v = 3*t**2 - 6*t + 2
# aceleração
a = 6*t-6

plt.figure(figsize=(10,6))

# Posição
plt.subplot(3,1,1,)
plt.plot(t,x,'b')
plt.title("Posição x(t) = t³-3t² + 2t")
plt.axhline(0, color='black', lw=0.5)
plt.grid(True)

# Velocidade
plt.subplot(3,1,2)
plt.plot(t,v,'g')
plt.title("Velocidade v(t) = 3t²- 6t +2")
plt.axhline(0, color="black", lw= 0.5)
plt.grid(True)

# Aceleração
plt.subplot(3,1,3)
plt.plot(t,a,'r')
plt.title("Aceleração a(t) = 6t-6")
plt.axhline(0, color='black', lw=0.5)
plt.grid(True)
plt.tight_layout()
plt.show()

