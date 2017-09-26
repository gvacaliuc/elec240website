### ELEC 240 Lab 

# Introduction 

In Lab 3 we saw that the voltage divider was an attenuator: 

$$
v_{out} = \frac{R_2}{R_1 + R_2} v_{in} = G v_{in}
$$  

where $G \le 1$. Let's consider a blackbox with an input voltage $v_{in}$ and an output voltage $v_{out}$ = G v_{in}$ with $G > 1$. This black box would be an *amplifier*. To be more precise, we would have a *non-inverting*,
*voltage* amplifier. If $G < -1$, we would still be increasing the magnitude
of the signal, but would invert its sign. This is called an *inverting*
amplifier.  

Similarly, a *current amplifier* would be described as $i_{out} = G_i i_{in}$.
Circuits containing only resistors, capacitors, and inductors are *passive*. An amplifier is an *active* circuit
element; it delivers more power to its load than it receives from its source.
This additional power comes from an external power supply, so no laws
of physics are being violated, but when we are drawing circuit diagrams we
usually only draw the amplifier and ignore the power supply.
