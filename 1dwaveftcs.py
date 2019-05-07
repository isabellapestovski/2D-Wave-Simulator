#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:54:59 2019

@author: isabellapestovski
"""
from numpy import zeros,array,linspace,nan
from math import sin,pi,sqrt,exp,cos
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
#sigma = 0.5
#dx = 0.01
#dt = sqrt(dx*dx*sigma)

dx = 0.01
dt = 0.00707
c = 1
r = c*dt/dx

lenx = int(1/dx)+1
lent = int(1/dt)+1

t = array([linspace(0,1,lent)])
x = array([linspace(0,1,lenx)])


u = zeros([lenx,lent])

# initial displacement condition
# for single pulse
def init_fn(x):
    return 0
# standing wave
#def init_fn(x):
#    return sin(3*pi*x)
# split wave propagation
#def init_fn(x):
#    return -cos(3*pi*x)*sin(pi*x)

# intial velocity condition
def g(x):
   return 1
# initially at rest
#def g(x):
#    return 0

# set up initial displacement condition on x    
for i in range(lenx):
    u[i,0]=init_fn(i*dx)

# set up initial velocity condition on x
#for j in range(1,lenx-1):
#     u[j,1] = sigma*(u[j+1,0]-2*u[j,0]+u[j-1,0]) + u[j,0]
for j in range(1,lenx-1):
     u[j,1] = 0.5*(r**2*u[j+1,0]+2*(1-r**2)*u[j,0]+r**2*u[j-1,0]) + dt*g(j*dx)

# algorithm to numerically solve wave equation
#for n in range(1,lent-1):
#    for j in range(1,lenx-1):
#        u[j,n+1] = sigma*(u[j+1,n] - 2*u[j,n] + u[j-1,n]) + 2*u[j,n] - u[j,n-1]
     
for n in range(1,lent-1):
    for j in range(1,lenx-1):
        u[j,n+1] = r**2*u[j+1,n] + 2*(1-r**2)*u[j,n] + r**2*u[j-1,n] - u[j,n-1]

fig, ax = plt.subplots()

line, = ax.plot(x.transpose(), u[:,0])
line.set_ydata([nan] * lenx)
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([nan] * lenx)
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    ax.set_ylim(-1,1)
    return line,

def animate(i):
    line.set_ydata(u[:,i])  # update the data.
    ax.set_ylim(-1,1)
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=20, blit=True, save_count=142)
ani.save('pulse.gif', writer='imagemagick', fps=60)
#plt.show()