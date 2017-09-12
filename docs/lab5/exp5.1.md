ELEC 240 Lab

------------------------------------------------------------------------

Experiment 5.1
--------------

Function Generator
------------------

### Equipment

-   Test board
-   LM741 (4x)
-   Resistors according to your design
-   Capacitors according to your design

### Part A: Build a Function Generator

In this lab experiment, we will be building our own function generator
using two new types of op amp circuits.

- Wire up the following RC relaxation oscillator circuit (see
Introduction to read about its functionality):\
![](../figs/multivib.png){width="559" height="391"}\
\

- **Is the output as expected? Provide a screenshot in your report.**

- **What is the frequency of oscillation?**

o The frequency should be equal to \$f = \\frac{1}{2.2\*R1\*C1}\$. Is
this what you measure?****

- **Does the frequency change as expected when R1 is changed?**

- Cascade an integrator circuit to the output as shown below:\
![](../figs/integrator.png){width="580" height="264"} ****

- **Is the integrator working as expected? Explain and provide a
screenshot.**

- Measure the DC offset of Vout2. ****

o *Note: DC offset is the average voltage of your waveform.*****

- Eliminate the DC offset by placing a DC blocking capacitor (any
capacitor between 0.1uF and 1uF) in between the RC relaxation oscillator
and integrator. **Provide a screenshot.**

- Now add on to your circuit so that it also generates a sinusoid.
**Provide a screenshot.**

- Build a gain stage to your circuit to modulate the amplitude of your
sinusoidal output.****
