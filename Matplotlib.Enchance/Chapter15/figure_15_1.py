import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt

# set sample data
x = np.linspace(0,10,10000)
y = np.sin(x)*np.cos(x)

plt.plot(x,y,ls="-",lw=2,color="c",alpha=0.3)

plt.text(1,0.5,r"\mathrm{Roman}:$\mathrm{Roman}\/(1st)$",fontsize=15)
plt.text(1,0.4,r"\mathit{Italic}:$\mathit{Italic}\/(2nd)$",fontsize=15)
plt.text(1,0.3,r"\mathtt{Typewriter}:$\mathtt{Typewriter}\/(3rd)$",fontsize=15)
plt.text(1,0.2,r"\mathcal{CALLIGRAPHY}:$\mathcal{CALLIGRAPHY}\/(4th)$",fontsize=15)
plt.text(1,0.1,r"\mathbb{blackboard}:$\mathbb{blackboard}\/(5th)$",fontsize=15)
plt.text(1,0.0,r"\mathfrak{Fraktur}:$\mathfrak{Fraktur}\/(6th)$",fontsize=15)
plt.text(1,-0.1,r"\mathsf{sansserif}:$\mathsf{sansserif}\/(7th)$",fontsize=15)
plt.text(1,-0.2,r"\mathcircled{circled}:$\mathcircled{circled}\/(8th)$",fontsize=15)
plt.text(1,-0.3,r"\mathrm{\mathbb{blackboard}}:$\mathrm{\mathbb{blackboard}}\/(9th)$",fontsize=15)

plt.show()
