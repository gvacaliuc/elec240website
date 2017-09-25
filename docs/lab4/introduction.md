### ELEC 240 Lab 

# Introduction 

In Lab 3 we saw that the voltage divider was an attenuator: 

$$
v_{out} = \frac{R_2}{R_1 + R_2} v_{in} = G v_{in}
$$  

where $G \le 1$. If we had a box where $v_{out} = G v_{in}$ with $G > 1$ we
would have an *amplifier*. To be more precise, we would have a *non-inverting*,
*voltage* amplifier. If $G < -1$, we would still be increasing the magnitude
of the signal, but would change its sign. This is called an *inverting*
amplifier.  

We could also have a *current amplifier* where $i_{out} = G_i i_{in}$.
Circuits containing only resistors, capacitors, and inductors (e.g.
attenuators or RC filters) are *passive*. An amplifier is an *active* circuit
element; it delivers more power to its load than it receives from its source.
(In fact this additional power comes from an external power supply, so no laws
of physics are being violated, but when we're drawing circuit diagrams we
usually draw only the amplifier and ignore the power supply.)
