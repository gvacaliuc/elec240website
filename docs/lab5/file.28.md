\#\#\# ELEC 240 Lab \# Introduction This week we are going to look at
some more types of op amp circuits. Using these op amp circuits, we will
build our own function generator. The first type of op amp circuit is a
square-wave generator, or also called an RC relaxation oscillator. We do
this by operating the op amp as a comparator. A comparator's output
toggles between +Vcc and -Vcc at a frequency dependent on the
charge/discharge rate of a capacitor through a feedback resistor. When
the output is high the capacitor charges. Once the voltage across the
capacitor reaches a certain positive reference voltage, the output is
driven negative. Once the capacitor charges to the negative reference
voltage, the output is driven high. With positive feedback, this cycle
continues and we see a square wave oscillation on the output. The
frequency of the oscillation is \$f = \\frac{1}{2\*RC}\$. Next we will
create an integrator, which performs the mathematical operation of
integration with respect to time. How could we use an integrator to
create different waveform shapes for our function generator? The
integrator works by passing a current that charges or discharges a
capacitor in the negative feedback loop. To analyze an integrator, first
assume that the opamp is ideal. The integrator looks like as below,
![](../figs/img202.png){width="399" height="225"}
and uses the ideal constraints below.
\$i\_f + i\_s = 0\$ \$v\_n = v\_p\$
We can define the currents as
\$i\_s = \\frac{v\_s}{R\_s}\$ \$i\_f = {C\_f}\\frac{dv\_o}{dt}\$
with substitution into the first ideal constraint equation
\$\\frac{dv\_o}{dt} = - {\\frac{1}{{R\_s}C\_f}}{v\_s}\$
and multiplying both sides by \$dt\$ and integrate:
\$v\_o = - {\\frac{1}{{R\_s}C\_f}}\\int\_{t\_o}\^t {v\_s}dt +
v\_o(t\_o)\$
The equation states that the output voltage of an integrator equals the
initial value of the voltage plus an inverted, scaled, replica of the
integral of the input voltage. If the initial voltage is zero, then the
output reduces to:
\$v\_o = - {\\frac{1}{{R\_s}C\_f}}\\int\_{t\_o}\^t {v\_s}dt\$
Finally we will amplify our output with an inverting amplifier like we
built last time.
