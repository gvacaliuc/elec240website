ELEC 240 Lab

------------------------------------------------------------------------

Experiment 4.1
--------------

The 741 Op-Amp
--------------

### 

### Equipment

-   741 Op Amp
-   10 Ω Resistor
-   10 kΩ Resistor
-   100 Ω Resistor

### Part A: Powering up the 741 Op Amp

The 741 operational amplifier, or op-amp, comes in an 8-pin dual inline
package (DIP) which looks like this:\
![](../figs/741_photo2.jpg){width="357" height="187"}

If you look closely at the package, you will find a notch at one end or
a dot in one corner. This tells us how to find Pin 1: the dot is located
next to Pin 1 and the notch is located between Pins 1 and 8. The rest of
the pins are numbered like this:\
![](../figs/741_pkg.gif){width="560" height="308"}\
Pin 8 is not connected (NC). Pins 1 and 5 are used to eliminate the
offset voltage. We won't be using this feature, so don't connect
anything to these pins. The remaining pins give us the following circuit
symbol for our op-amp:\
![](../figs/img173.png){width="267" height="135"}\

For more information, see the []()[741 data
sheet](http://www.ti.com/lit/ds/symlink/lm741.pdf).

In order to function, the op-amp must be connected to an external *power
supply*. Since we want to produce both positive and negative output
voltages, we need both positive and negative voltages for the power
supply. These are labeled V~CC+~ and V~CC-~ on the diagram. For a 741,
the nominal values are V~CC+~=15 V and V~CC-~=-15 V.

To avoid clutter, we won't show the power supply terminals (pins 4 and
7) on any of the subsequent circuit diagrams. However, they must be
connected or your amplifier will not operate.

Note that there is no ground terminal on the op-amp. The zero reference
point is established by the external circuit and is not important to the
op-amp itself.

- If you have not already done so, wire the bus strips on your
breadboard to provide positive power, negative power and ground buses.
Whatever color scheme you have chosen for your wires, you should use the
green binding post for ground, the black for -15 V, and the red for +15
V.

- Plug an op-amp into the breadboard so that it straddles the gap
between the top and bottom sections of the socket strip. If you have
wired the power buses as suggested above, Pin 1 should be to the left.

o *Warning: Do not try to unplug the op-amp with your thumb and
forefinger. It's a good way to end up with the op-amp plugged into your
fingertip. Use the pliers or []()[IC puller](/misc_images/#ic-puller)
from your toolkit.*

- Connect Pin 4 (V~CC-~) to the negative power supply bus (-15 V).
Connect Pin 7 (V~CC+~) to the positive power supply bus (+15 V).\
*![](../figs/opamp_pwr.jpg){width="320" height="240"}*

- Set up the +/- 25V power supply dongle. Turn on the power supply and
set the VirtualBench voltage control to 15 volts.

- Turn off the supply and connect the supply to the breadboard with
banana plug patch cables. Connect the -25V terminal to the black binding
post on your breadboard, the+25V terminal to the red breadboard binding
post, and the GROUND terminal to the green breadboard binding post. Note
that none of the power supply output terminals are connected to ground.
If we want the power supply zero volt reference connected to ground, we
must make the connection ourselves.

### Part B: Open-Loop Response

- With the power turned off, wire the following circuit. Note that the
input to the op amp is a 1000:1 voltage divider, so that a 1 V signal at
v ~in~ results in a 1 mV signal at the input of the op-amp.

o *Caution: The components we've used so far have been simple (only two
terminals) and fairly rugged (connecting a resistor or capacitor
"backwards" won't harm it). The op-amp has four times as many pins, so
it's easier to make a mistake in wiring it. Unfortunately, it's also
considerably more delicate, so connecting it incorrectly can destroy it
(often without so much as a puff of smoke to let you know that it has
become an inoperational amplifier.\
Always wire your circuit with the power turned off and check your wiring
carefully before turning the power on.\
![](../figs/img174.png){width="390" height="109"}\
![](../figs/open_loop.jpg){width="320" height="240"}*

- Set the function generator to produce a 2 V p-p, 20 Hz sine wave.

- Connect the function generator output to v~in~ of the circuit above.
Connect CH1 of the scope to v~in~ and CH2 to v~out~. Set theCH2
VOLTS/DIV to 5. Make sure both channels of the scope are on DC.

- You should see a badly distorted (clipped) waveform at v~out~. If you
don't, try increasing the function generator output.

- Adjust the distorted waveform (will look like a square wave) so that
it is symmetric about the x-axis. **Note the positive and negative peak
values of v~out~.**

- Connect a 100Ω resistor from v~out~ to ground. **What happens to the
output signal?**

- Remove the 100Ω resistor from the op amp output.

- Set the FGEN to square wave. **Now what is the shape of the v~out~
waveform?** Does the output change slope as fast as the input does? This
is called slew-rate limiting.

- Make sure the DC offset on the FGEN is zero. **Does the output also
show zero DC offset?**

o We have just seen a number of the shortcomings of a real (as opposed
to an ideal) operational amplifier: clipping, which limits the maximum
amplitude of the output; slew-rate limiting, which limits the maximum
slope of the output; and offset, which gives a non-zero output for zero
input.

o When we reduce the overall gain with feedback, some of these (e.g.
offset) are reduced significantly, and we get an output which is a
faithful reproduction of the input. However, other limits (such as
maximum output level) must be respected for this fidelity to remain.

- **Summarize why, if we want to amplify our signal with an op-amp,
operating it in open loop is not the ideal solution.**

****
