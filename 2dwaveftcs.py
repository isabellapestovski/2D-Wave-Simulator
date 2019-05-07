#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:34:57 2019

@author: isabellapestovski
"""
from numpy import zeros,array,linspace,meshgrid
from math import sqrt,sin,exp,pi,cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

sigma = 0.5
dx = 0.01
dy = dx
dt = sqrt(dx*dx*sigma)

lenx = int(1/dx)+1
leny = int(1/dy)+1
lent = int(1/dt)+1

t = array([linspace(0,1,lent)])
x = array([linspace(0,1,lenx)])
y = array([linspace(0,1,leny)])

u = zeros([lenx,leny,lent])

# wave split propagation
#def init_fn(x,y):
#    return -cos(3*pi*x)*sin(pi*x)*-cos(3*pi*y)*sin(pi*y)
# standing wave
#def init_fn(x,y):
#    return sin(3*pi*x)*sin(3*pi*y)
# ripple propagation
def init_fn(x,y):
    return exp(-(2*pi*x)**2)*sin(2*pi*x)*exp(-(2*pi*y)**2)*sin(2*pi*y)

for i in range(lenx):
    for j in range(leny):
        u[i,j,0] = init_fn(i*dx,j*dy)

for i in range(1,lenx-1):
    for j in range(1,leny-1):
        u[i,j,1] = sigma*(u[i+1,j,0]-2*u[i,j,0]+u[i-1,j,0]) +\
        sigma*(u[i,j+1,0]-2*u[i,j,0]+u[i,j-1,0]) + u[i,j,0]

# algorithm to numerically solve wave equation
for n in range(1,lent-1):
    for i in range(1,lenx-1):
        for j in range(1,leny-1):
            u[i,j,n+1] = sigma*(u[i+1,j,n] - 2*u[i,j,n] + u[i-1,j,n]) +\
            sigma*(u[i,j+1,n]-2*u[i,j,n]+u[i,j-1,n]) + 2*u[i,j,n] - u[i,j,n-1]

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y = meshgrid(x.transpose(),y.transpose())
Z = u[:,:,0]
plot = Axes3D.plot_surface(ax,X,Y,Z)
ax.set_zlim3d(-1,1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

def update_plot(i,u,plot):
    ax.clear()
    plot = Axes3D.plot_surface(ax,X,Y,u[:,:,i], cmap="magma")
    ax.set_zlim3d(-1,1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    return plot

ani = animation.FuncAnimation(fig,update_plot,fargs=(u, plot))
ani.save('ripple2d.gif', writer='imagemagick', fps=60)