import numpy as np
import matplotlib.pyplot as plt


def I(delta_k):
    return (np.sin( 2 * delta_k))**2 / ( 2 *delta_k )**2


Dk = np.linspace(-2*np.pi, 2*np.pi, 1e5)


plt.figure(figsize=(16, 9))
plt.plot(Dk, I(Dk))
plt.ylabel(r'$\Gamma \, / \, \mathrm{a.u.} $')
plt.xlabel(r'$\Delta k \, / \, \mathrm{a.u.} $')

plt.savefig('./efficiency_second_harmonic.png',  bbox_inches='tight')
