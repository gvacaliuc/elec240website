ELEC 240 Lab

------------------------------------------------------------------------

Experiment 4.2
--------------

The Inverting Configuration
---------------------------

### 

### Equipment

-   741 Op Amp
-   10 kΩ Resistors (2)

As we saw in the previous experiment, the op-amp isn't very useful in an
"open-loop" configuration (i.e. without feedback). The most common
configuration for op-amp circuits is the *inverting amplifier* where the
output is an amplified and inverted version of the input (i.e. G is
negative).

### Part A: The Basic Inverting Amplifier

- Wire the following circuit using 10 kΩ resistors for both R~1~ and
R~F~.\
\
![](../figs/img175.png){width="332" height="187"}

- Set the function generator to produce a 1 V p-p, 100 Hz sine wave.
Measure the voltage gain, G~v~=V~out~/V~in~. Since 100 Hz is within the
frequency range of the DMM, you could use either the DMM or the scope to
measure V~out~ and V~in~. However, you should always use the scope to
*view* the waveform being measured to make sure it is what you think it
is. We will see several waveforms in this lab that aren't.

- Note that the output is inverted with respect to the input. **Take a
screenshot for your report.**

- Replace R~F~ with a 100 kΩ resistor. **Measure the gain.**

- Increase the input amplitude until output clipping occurs. **What is
the clipping level? Is it the same as in Exp. 4.1?**

- Reduce the input amplitude until the output is 20 V p-p.

- Increase the frequency until the output amplitude drops to 10 V p-p**.
You should see a triangular output waveform**. This is because there is
a limit to the maximum rate at which the output voltage can change,
called the *slew rate.* **Set the input to triangle and square wave and
see how the output changes.**

- Reset the function generator for a 100 Hz sine wave and reduce the
amplitude to produce a 1 V p-p output. Again increase the frequency
until the output is 0.7 V p-p. **At what frequency does this occur?**
Observe that the output is still sinusoidal. This is the actual cutoff
frequency or *bandwidth* of the amplifier.
