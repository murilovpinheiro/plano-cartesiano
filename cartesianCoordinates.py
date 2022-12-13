import matplotlib.pyplot as plt
import numpy as np
import math

def Angle(T1, T2):
    print(T1[1], T2[1])
    return (math.atan((T2[0] - T1[0])/(T1[1] - T2[1])))

def createCartesianPlan(start, end, frequency, quantity):
    fig, axes = plt.subplots(figsize = (12, 10), nrows = quantity)
    fig.patch.set_facecolor('#ffffff')
    if quantity > 1:
        for ax in axes:
            ax.set(xlim = (start - 0.3 , end + 1), ylim = (start - 0.3 , end + 1), aspect = "equal")

            ax.spines['bottom'].set_position('zero')
            ax.spines['left'].set_position('zero')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

            ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
            ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

            x_ticks = np.arange(start, end+1, frequency)
            y_ticks = np.arange(start, end+1, frequency)

            ax.set_xticks(x_ticks[x_ticks != 0])
            ax.set_yticks(y_ticks[y_ticks != 0])
            ax.set_xticks(np.arange(start, end + 1), minor=True)
            ax.set_yticks(np.arange(start, end + 1), minor=True)

            ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    else: 
            axes.set(xlim = (start - 0.3 , end + 1), ylim = (start - 0.3 , end + 1), aspect = "equal")

            axes.spines['bottom'].set_position('zero')
            axes.spines['left'].set_position('zero')
            axes.spines['top'].set_visible(False)
            axes.spines['right'].set_visible(False)

            axes.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
            axes.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

            x_ticks = np.arange(start, end+1, frequency)
            y_ticks = np.arange(start, end+1, frequency)

            axes.set_xticks(x_ticks[x_ticks != 0])
            axes.set_yticks(y_ticks[y_ticks != 0])
            axes.set_xticks(np.arange(start, end + 1), minor=True)
            axes.set_yticks(np.arange(start, end + 1), minor=True)

            axes.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    return fig, axes

#cria a equação linear a partir dos pontos oferecidos
def linearEquation(v1, v2):
    x = np.linspace(0 , 1, 500)
    y = np.linspace(1, 0, 500)
    x1 = v1 * x + v2 * 0
    y1 = v1 * 0 + v2 * y
    return (x1, y1)

# #cria uma reta com os pesos estabelecidos variando em x e em y
# def ray(w1, w2):
#     x = np.linspace(0 , 4, 500)
#     y = np.linspace(0, 4, 500)
#     return (x * w1, y * w2)

def plotLinearEquation(ax, list):
    linEq = ()
    size = ax.get_xlim()    
    for I in range(len(list)):
        linEq =  linearEquation(list[I][0], list[I][1])
        ax.plot(linEq[0], linEq[1], "#0000cc", linewidth = 1)
    ax.set_title("Exemplo equação linear")
    # line = ray(1, 1)

def plotFunction(ax, function, linestyle):
    size = ax.get_xlim()
    xValues = np.linspace(0, size, 100)
    ax.set_title("Exemplo função de x")
    ax.plot(xValues, function(xValues), linestyle, linewidth = 1.5)

def plotPoint(ax, point):
    ax.plot(point[0], point[1], "o")
list = [[0.5, 0.5], [0.65, 0.05], [2, 2],[1.5, 0.1],[1.2, 1]]
print()
fig, ax = createCartesianPlan(0, 5, 1, 1)
for i in list:
    plotPoint(ax, i)

coeficiente = 1/3 #
distanciamento = 2 # valores somados de x*w1 + y*w2 para passar pelo ponto x,y
plotFunction(ax, lambda x: coeficiente*x, 'b-')
plotFunction(ax, lambda x: -1/coeficiente*x + distanciamento, 'r-')
distanciamento = 4.6 # valores somados de x*w1 + y*w2 para passar pelo ponto x,y
plotFunction(ax, lambda x: -1/coeficiente*x + distanciamento, 'g--')
# TUDO APARANTEMENTE OK
fig.savefig("Grafico.png", bbox_inches='tight', pad_inches = 0.5)