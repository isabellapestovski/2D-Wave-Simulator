# 2D-Wave-Simulator

The wave equation is an important equation in mathematics and physics describing the oscillation of particles in space. Solutions to the wave equation demonstrate the motion of mechanical as well as electromagnetic waves. In order to solve the equation, two initial conditions and four boundary conditions need to be specified. This educational tool allows students to explore the effects of various initial conditions to understand the behavior of wave propagation as well as how to mathematically model physical phenomena. 

1dwaveftcs.py uses the forward-time centered-space method to numerically solve the 1D wave equation for a string of unit length and fixed displacement at the ends. Three different initial conditions are solved to produce animations using Matplotlib. The initial conditions demonstrate single pulse, standing wave, and split propagation behavior. The animations are saved as gifs and then used in GUI1D.ipnyb

2dwaveftcs.py uses the forward-time centered-space method to numerically solve the 2D wave equation for a plane of unit area and fixed displacement at the edges. Three different initial conditions are solved to produce animations using Matplotlib. The initial conditions demonstrate standing wave, ripple, and split propagation behavior. The animations are saved as gifs and then used in GUI2D.ipnyb

The GUI files produce a GUI home screen with buttons that direct the user to a page with a looped animation of the solution to the wave equation.
