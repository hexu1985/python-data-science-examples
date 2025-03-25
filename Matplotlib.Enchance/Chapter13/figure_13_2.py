import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages

with PdfPages("./PdfPages.pdf") as pdf:

    # page one
    plt.figure(figsize=(4,4))
    x = np.random.rand(20)*100
    y = np.random.rand(20)*100+30
    s = np.random.rand(20)*100
    c = np.random.rand(20)
    data = {"a":x,"b":y,"color":c,"size":s}
    plt.scatter("a","b",c="color",s="size",data=data)
    plt.title("Page1")
    pdf.savefig()  # save the current figure
    plt.close()  # close the current figure

    # page two
    fig = plt.figure(figsize=(8,6))
    x = np.linspace(0,2*np.pi,100)
    y1 = 0.5*np.cos(x)
    y2 = 0.5*np.sin(x)
    plt.plot(y1,y2,color="navy",lw=3)
    plt.axis("equal")
    plt.title("Page2")
    pdf.savefig(fig)  # pass the Figure instance fig to pdf.savefig
    plt.close(fig)  # close the Figure instance fig

    # page three
    fig,ax = plt.subplots(1,2)
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)*np.exp(-x)
    ax[0].scatter(x,y,c="cornflowerblue",s=100)
    ax[1].plot(x,y,"k-o",lw=2)
    ax[1].set(xlim=(-1,7))
    fig.suptitle("Page3")
    pdf.savefig(fig)
    plt.close(fig)
