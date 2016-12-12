
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 4.1
</h2>
<h2>
The 741 Op-Amp
</h2>
</center>
<h3>

<h3>
    Equipment
</h3>
<ul>
<li>741 Op Amp
<li>10 &#8486; Resistor
<li>10 k&#8486; Resistor
<li>100 &#8486; Resistor
</ul>
<h3>
    Part A: Powering up the 741 Op Amp
</h3>
<p>
    The 741 operational amplifier, or op-amp, comes in an 8-pin dual inline package (DIP) which looks like this:
    <br/>
    <img width="357" height="187" src="../figs/741_photo2.jpg"/>
</p>
<p>
    If you look closely at the package, you will find a notch at one end or a dot in one corner. This tells us how to find Pin 1: the dot is located next to
    Pin 1 and the notch is located between Pins 1 and 8. The rest of the pins are numbered like this:
    <br/>
    <img width="560" height="308" src="../figs/741_pkg.gif"/>
    <br/>
    Pin 8 is not connected (NC). Pins 1 and 5 are used to eliminate the offset voltage. We won't be using this feature, so don't connect anything to these
    pins. The remaining pins give us the following circuit symbol for our op-amp:
    <br/>
    <img width="267" height="135" src="../figs/img173.png"/>
    <br/>
<p>    For more information, see the <a name="741"></a><a href="http://www.ti.com/lit/ds/symlink/lm741.pdf">741 data sheet</a>.
    </p>
    In order to function, the op-amp must be connected to an external <em>power supply</em>. Since we want to produce both positive and negative output
    voltages, we need both positive and negative voltages for the power supply. These are labeled V<sub>CC+</sub> and V<sub>CC-</sub> on the diagram. For a
    741, the nominal values are V<sub>CC+</sub>=15 V and V<sub>CC-</sub>=-15 V.
</p>
<p>
    To avoid clutter, we won't show the power supply terminals (pins 4 and 7) on any of the subsequent circuit diagrams. However, they must be connected or
    your amplifier will not operate.
</p>
<p>
    Note that there is no ground terminal on the op-amp. The zero reference point is established by the external circuit and is not important to the op-amp
    itself.
</p>
<p>
    - If you have not already done so, wire the bus strips on your breadboard to provide positive power, negative power and ground buses. Whatever color scheme
    you have chosen for your wires, you should use the green binding post for ground, the black for -15 V, and the red for +15 V.
</p>
<p>
    - Plug an op-amp into the breadboard so that it straddles the gap between the top and bottom sections of the socket strip. If you have wired the power
    buses as suggested above, Pin 1 should be to the left.
</p>
<DT>
<DD><p>
    o
    <em>
        Warning: Do not try to unplug the op-amp with your thumb and forefinger. It's a good way to end up with the op-amp plugged into your fingertip. Use the
        pliers or <a name="IC"></a><a href=/misc_images/#ic-puller>IC puller</a> from your toolkit.
    </em>
</p></DD>
<p>
    - Connect Pin 4 (V<sub>CC-</sub>) to the negative power supply bus (-15 V). Connect Pin 7 (V<sub>CC+</sub>) to the positive power supply bus (+15 V).
    <br/>
    <em>
        <img border="0" width="320" height="240" src="../figs/opamp_pwr.jpg"/>
    </em>
</p>
<p>
    - Set up the +/- 25V power supply dongle. Turn on the power supply and set the VirtualBench voltage control to 15 volts.
</p>
<p>
    - Turn off the supply and connect the supply to the breadboard with banana plug patch cables. Connect the -25V terminal to the black binding post on your
    breadboard, the+25V terminal to the red breadboard binding post, and the GROUND terminal to the green breadboard binding post. Note that none of the power
    supply output terminals are connected to ground. If we want the power supply zero volt reference connected to ground, we must make the connection
    ourselves.
</p>
<h3>
    Part B: Open-Loop Response
</h3>
<p>
- With the power turned off, wire the following circuit. Note that the input to the op amp is a 1000:1 voltage divider, so that a 1 V signal at v    <sub>in</sub> results in a 1 mV signal at the input of the op-amp.
</p>
<DD><p>
    o
    <em>
        Caution: The components we've used so far have been simple (only two terminals) and fairly rugged (connecting a resistor or capacitor "backwards" won't
        harm it). The op-amp has four times as many pins, so it's easier to make a mistake in wiring it. Unfortunately, it's also considerably more delicate,
        so connecting it incorrectly can destroy it (often without so much as a puff of smoke to let you know that it has become an inoperational amplifier.
        <br/>
        Always wire your circuit with the power turned off and check your wiring carefully before turning the power on.
        <br/>
        <img border="0" width="390" height="109" src="../figs/img174.png"/>
        <br/>
        <img border="0" width="320" height="240" src="../figs/open_loop.jpg"/>
    </em>
</p></DD>
<p>
    - Set the function generator to produce a 2 V p-p, 20 Hz sine wave.
</p>
<p>
    - Connect the function generator output to v<sub>in</sub> of the circuit above. Connect CH1 of the scope to v<sub>in</sub> and CH2 to v<sub>out</sub>. Set
    theCH2 VOLTS/DIV to 5. Make sure both channels of the scope are on DC.
</p>
<p>
    - You should see a badly distorted (clipped) waveform at v<sub>out</sub>. If you don't, try increasing the function generator output.
</p>
<p>
- Adjust the distorted waveform (will look like a square wave) so that it is symmetric about the x-axis.    <strong>Note the positive and negative peak values of v<sub>out</sub>. </strong>
</p>
<p>
    - Connect a 100&#8486; resistor from v<sub>out</sub> to ground.<strong> What happens to the output signal?</strong>
</p>
<p>
    - Remove the 100&#8486; resistor from the op amp output.
</p>
<p>
    - Set the FGEN to square wave.<strong> Now what is the shape of the v<sub>out</sub> waveform?</strong> Does the output change slope as fast as the input
    does? This is called slew-rate limiting.
</p>
<p>
    - Make sure the DC offset on the FGEN is zero. <strong>Does the output also show zero DC offset?</strong>
</p>
<DD><p>
    o We have just seen a number of the shortcomings of a real (as opposed to an ideal) operational amplifier: clipping, which limits the maximum amplitude of
    the output; slew-rate limiting, which limits the maximum slope of the output; and offset, which gives a non-zero output for zero input.
</p></DD>
<DD><p>
    o When we reduce the overall gain with feedback, some of these (e.g. offset) are reduced significantly, and we get an output which is a faithful
    reproduction of the input. However, other limits (such as maximum output level) must be respected for this fidelity to remain.
</p></DD>
<p>
    - <strong>Summarize why, if we want to amplify our signal with an op-amp, operating it in open loop is not the ideal solution. </strong>
</p>
<p>
    <strong> </strong>
</p>
</DT>
