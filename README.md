# FDTD EM Propagation
This is a collection of my implementation of code from ['Understanding the FDTD Method' by John. B Schneider](https://eecs.wsu.edu/~schneidj/ufdtd/).

## Background
Initially, I implemented this code into Swift in a group project during my 1st year as a physics student. Now, while working on my skills as a software developer, I'm re-coding this project into Python, due to the easier graphing functionality.

# Programs:

## 1DbareBones.py - Program 3.1:
This is the first EM propagation program in the book, Program 3.1, showing the propagation of an EM wave through free space across a grid of size 200.

## 1Dadditive.py - Program 3.4:
Building on 1DbareBones.py, this program uses an additive source at node 50.

## generateWaterfall.py:
This program, given a multi-dimensional array, will create a waterfall plot from the given data.

## 1Dtfsf.py - Program 3.5:
Implements a Total-Field Scattered-Field.

## 1Ddielectric.py - Program 3.6:
Simulates a dielectric with a relative permittivity of 9 from node 100, and free space before node 100.

## 1Dlossy.py - Program 3.7:
Simulates a lossy dielectric to the right of node 100, free space to the left.

## 1Dmatched.py - Program 3.8:
Simulates a lossless dielectric region followed by a lossy layer with impedance matched to the lossless dielectric.

## improved1.py - Program 4.6:
Improved version of the 1DbareBones.py code, which implements a Grid object. This grid will become more useful as we progress to more complex simulations.