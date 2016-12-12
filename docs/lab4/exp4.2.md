
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 4.2
</h2>
<h2>
The Inverting Configuration
</h2>

</center>
<h3>

<h3>
    Equipment
</h3>
<ul>
<li>741 Op Amp
<li>10 k&#8486; Resistors (2)
</ul>
<p>
    As we saw in the previous experiment, the op-amp isn't very useful in an "open-loop" configuration (i.e. without feedback). The most common configuration
    for op-amp circuits is the <em>inverting amplifier</em> where the output is an amplified and inverted version of the input (i.e. G is negative).
</p>
<h3>
    Part A: The Basic Inverting Amplifier
</h3>
<p>
    - Wire the following circuit using 10 k&#8486; resistors for both R<sub>1</sub> and R<sub>F</sub>.
    <br/>
    <br/>
    <img width="332" height="187" src="../figs/img175.png"/>
</p>
<p>
    - Set the function generator to produce a 1 V p-p, 100 Hz sine wave. Measure the voltage gain, G<sub>v</sub>=V<sub>out</sub>/V<sub>in</sub>. Since 100 Hz
    is within the frequency range of the DMM, you could use either the DMM or the scope to measure V<sub>out</sub> and V<sub>in</sub>. However, you should
    always use the scope to <em>view</em> the waveform being measured to make sure it is what you think it is. We will see several waveforms in this lab that
    aren't.
</p>
<p>
    - Note that the output is inverted with respect to the input. <strong>Take a screenshot for your report.</strong>
</p>
<p>
    - Replace R<sub>F</sub> with a 100 k&#8486; resistor. <strong>Measure the gain.</strong>
</p>
<p>
    - Increase the input amplitude until output clipping occurs. <strong>What is the clipping level? Is it the same as in Exp. 4.1?</strong>
</p>
<p>
    - Reduce the input amplitude until the output is 20 V p-p.
</p>
<p>
    - Increase the frequency until the output amplitude drops to 10 V p-p<strong>. You should see a triangular output waveform</strong>. This is because there
is a limit to the maximum rate at which the output voltage can change, called the <em>slew rate.</em>    <strong>Set the input to triangle and square wave and see how the output changes. </strong>
</p>
<p>
    - Reset the function generator for a 100 Hz sine wave and reduce the amplitude to produce a 1 V p-p output. Again increase the frequency until the output
is 0.7 V p-p.<strong> At what frequency does this occur? </strong>Observe that the output is still sinusoidal. This is the actual cutoff frequency or    <em>bandwidth</em> of the amplifier.
</p>
</DT>