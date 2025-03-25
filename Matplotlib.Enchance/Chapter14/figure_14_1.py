import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc,rcParams

rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]
rcParams["text.usetex"]=True
rc("font",**{"family":"sans-serif","sans-serif":["Helvetica"],"size":16})

# sample data
t = np.linspace(0.0,1.0,100)
s = np.cos(4*np.pi*t)+2

# plot figure
plt.plot(t,s,ls="-",lw=0.5,c="b")

# No.1 text
plt.text(0.2,2.8,r"$some\ ranges:(\alpha),[\beta],\{\gamma\},|\Gamma|,\Vert\phi\Vert,\langle\Phi\rangle$")

# No.2 text
# these went wrong in pdf in a previous version
plt.text(0.2, 2.5, r"gamma: $\gamma$", {"color": "r", "fontsize": 20})
plt.text(0.2, 2.3, r"Omega: $\Omega$", {"color": "b", "fontsize": 20})

# No.3 text
plt.text(0.2,2.0,r"$\lim_{i\to\infty}\cos(2\pi)\times\exp\{-i\}=0$")

# No.4 text
plt.text(0.2,1.5,r"$\mathrm{math\ equation}:\frac{n!}{(n-k)!}=\binom{n}{k}$",{"color": "c", "fontsize": 20})

# No.5 text
plt.text(0.2,1.2,r"$\forall\ i,\exists\ \alpha_i\geq\beta_i,\sqrt{\alpha_i-\beta_i}\geq{0}$")

# we can write labels with LaTeX
plt.xlabel(r"\textbf{time(s)}")
plt.ylabel(r"\textit{Velocity(m/s)}")

# and also write title with LaTex
plt.title(r"\TeX\ is Number $\displaystyle\sum_{n=1}^\infty"
             r"\frac{-e^{i\pi}}{2^n}$!", color="r")

plt.annotate(r"$\cos(4\times\pi\times{t})+2$",
             xy=(0.87,2.0),
             xytext=(0.65,2.3),
             color="r",
             arrowprops={"arrowstyle":"->","color":"r"})

plt.subplots_adjust(top=.8)

plt.show()
