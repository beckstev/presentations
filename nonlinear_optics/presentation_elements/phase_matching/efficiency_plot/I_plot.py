import numpy as np
import matplotlib.pyplot as plt


def I(delta_k):
    return (np.sin( 2 * delta_k))**2 / ( 2 *delta_k )**2


Dk = np.linspace(-2*np.pi, 2*np.pi, 1e5)


plt.figure(figsize=(16, 9))
plt.plot(Dk, I(Dk), linewidth=4)

plt.ylabel(r'$\Gamma \, / \, \mathrm{a.u.} $', fontsize=20)
plt.xlabel(r'$\Delta k \, / \, \mathrm{a.u.} $', fontsize=20)
plt.tick_params(axis='both', labelsize=20)

plt.savefig('./efficiency_second_harmonic.png',  bbox_inches='tight')
