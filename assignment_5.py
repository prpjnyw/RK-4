import matplotlib.pyplot as plt
import math

def graph_plot(x,y,xd,yd):
    plt.plot(xd, yd, marker='o', linestyle='-')
    plt.title("graph")
    plt.xlabel(f"{x}")
    plt.ylabel(f"{y}")
    plt.grid(True)
    plt.show()

# assignment5 /***** RK4 for solving y and y' value *****/
# y1 = y , y2 = y' 
# y1' = y2 , y2' = 0.5*y2 - 0.5*y1^2*y2 - y1

h = 0.01
y = [2 , -3] # y1 = y[0] y2 = y[1]
k1 = [] ; k2 = [] ; k3 = [] ; k4 = []
y_graph = []

def calc_k(y1,y2,k,i):
    x = h * y2 
    y = h * (0.5 * (y2 + i * k[1]) - 0.5 * ((y1 + i * k[0])**2) * (y2 + i * k[1]) - (y1 + i * k[0]))
    return [x,y]    

def clac_y_n(yn,k1,k2,k3,k4):
    x = yn[0] + 1/6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    y = yn[1] + 1/6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    return [x,y]

def RK_4(n):
    global y
    for i in range(n + 1):
        k1 = calc_k(y[0],y[1],[0,0],1)
        k2 = calc_k(y[0],y[1],k1,0.5)
        k3 = calc_k(y[0],y[1],k2,0.5)
        k4 = calc_k(y[0],y[1],k3,1)
        y = clac_y_n(y,k1,k2,k3,k4)
        y_graph.append(y)
        
RK_4(10)
# print(y)
# # print(y_graph)


regular_y = []
for i in range(10 + 1):
    regular_y.append(y_graph[i][0])

diff_y = []
for i in range(10 + 1):
    diff_y.append(y_graph[i][1])

X_axis = []
x = 0
for i in range(10 + 1):
    X_axis.append(round(x,2))
    x += h
   

# graph_plot("x","y",X_axis,regular_y)
# graph_plot("x","y'",X_axis,diff_y)
graph_plot("y","y'",regular_y,diff_y)
