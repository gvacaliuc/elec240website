ELEC 240 Lab

------------------------------------------------------------------------

Experiment 5.2
--------------

Frequency Response
------------------

### Equipment

-   Test board
-   Integrator from last experiment
-   1kΩ and 100Ω resistors
-   Lab computer or laptop

### Part A: Measuring Frequency Response

In this part of the lab you will use look at the frequency response of
your integrator.

- Disconnect the input and output from your integrator and modify it as
shown below. For the input, connect a 1 Vp-p sinusoidal signal from your
VirtualBench function generator.\
![](../figs/spiceintegrator.png){width="559" height="391"}\
\

- Record output peak-to-peak voltage values for the following
frequencies: 10Hz, 100Hz, 500 Hz, 800 Hz, 1kHz, 1.5kHz, 2kHz, 5kHz,
10kHz, 50kHz.

- Calculate the gain in decibels (dB) for your circuit at each of these
frequencies.

o \$Gain (dB) = 20\*log10(\\frac{Vout}{Vin})\$

- Plot \$Gain(dB)\$ vs. \$Frequency (Hz)\$ in Matlab. - At what
frequency does the gain begin to drop?

o **Does the cutoff frequency, \$f\_c\$ roughly equal
\$\\frac{1}{2\*\\pi\*R5\*C2}\$?**

### Part B: Circuit Simulation

The remainder of the lab can be done from a computer (lab computer or
personal laptop). We will be using circuit simulation software called
LTSpice. Spice stands for (Simulation Program with Integrated Circuit
Emphasis).

- Download LTspice from linear.com. There are Windows and Mac versions
available. Please note that the instructions below are specifically for
Windows.

- Click on New Schematic and create the same circuit you built on your
breadboard shown above.

o Place components by going to the Edit menu or shortcut buttons.

o The opamp is found under Edit-&gt;Components-&gt;\[OpAmps\]-&gt;opamp.
The voltage source is found under Edit-&gt;Components-&gt;voltage.
Connect components using Edit-&gt;Wire (or the shortcut button F3).

o Other convenient shortcuts are:

-   Ctrl-R for Rotate
-   Delete, or F5 for Delete
-   F6 for Copy
-   F7 for Move
-   F8 for Drag
-   Esc to exit out of a mode

o The component opamp is just a symbol of an opamp and in order for
Spice to see the model, you need to place a Spice Directive calling the
location: Edit-&gt;Spice Directive. Then enter .lib opamp.sub

o Set the voltage source to AC by right-clicking it and selecting
Advanced. Set AC amplitude to 1.

o Enter in R and C values by right-clicking these components.

o Optional MISSINGDATA label nets (i.e., wires) by right-clicking on
nets.

- Perform an AC analysis. An AC analysis will evaluate the gain
(Vout/Vin) and phase over a specified range of frequencies and plot it.

o Click on the Running Man icon and select AC analysis (or go to
Simulate-&gt;Run).

o Use a decade frequency sweep with at least 10 points per decade over
the range of 1 Hz to 10 MHz. This will appear as a Spice directive on
your schematic as

.ac dec 10 1 10meg

o Click on the Vout node for gain and phase plots to appear. You will
notice that the gain is displayed in dB and phase in degrees. The x-axis
will be logarithmic, i.e., the step size is \$10n\$, where \$n\$ is a
non-negative integer. Each of the steps is called a decade (dec).

- Take a screenshot of your plots.

- **What is the gain at low frequencies? What is the cutoff frequency?
What is the slope of the gain with respect to frequency for high
frequencies (express in terms of dB/dec)? Do these values match what you
measured on your breadboard?**

- **What is the phase for very low frequencies? At 0dB? And for very
high frequencies? Can you explain why?**
