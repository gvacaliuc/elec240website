
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 3.2
</h2>
<h2>
Filters and Transfer Function
</h2>
</center>
<h3>

<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>2.2 k&#8486; Resistor
<li>0.33 &#181;F <a href=/misc_images/#ceramic-caps2>Capacitor</a>
</ul>
<h3>
    Part A: Measuring the Transfer Function
</h3>
<p>
    Measuring the transfer function of an RC circuit is considerably more involved than measuring the attenuation of a resistive voltage divider. We have to
    make the measurement at a number of frequencies, and we must measure phase as well as amplitude.
</p>
<p>
- Select a 2.2 k&#8486; Resistor and a 0.33 &#181;F    <a href=/misc_images/#ceramic-caps2>Capacitor</a>.
</p>
<DT>
<DD><p>
    o Note: Ceramic capacitors use the same labeling codes as the potentiometers except that the units are picofarads (pF) instead of ohms. So a 0.33
    &#181;F capacitor would be a 330,000 pF capacitor which would have the code 334 (\(33*10^4\)).
</p></DD>
<p>
    - Wire the following circuit:
    <br/>
    <img border="0" width="208" height="143" src="../figs/img171.png"/>
</p>
<p>
    - Connect the FGEN to supply v<sub>in</sub> and the oscilloscope to measure v<sub>out</sub>.
</p>
<p>
    - Using the technique described in the previous section, measure the frequency response of the circuit at the following frequencies: 20 Hz, 50 Hz, 100 Hz,
    200 Hz, 500 Hz, 1 kHz, 2 kHz, 5 kHz, 10 kHz, and 20 kHz.
</p>
<p>
    - <strong>Plot the magnitude of the transfer function vs. frequency</strong> on loglog axes and the phase on semilog axes. This can be done by hand or in
    Matlab.
</p>
<p>
- Using Matlab, compute and plot the expected transfer function for the circuit you built.    <strong>How well does this compare with what you measured? </strong>
</p>
<p>
    - Leave this circuit assembled. We will use it in the next experiment.
</p>
<p>
    <strong> </strong>
</p>

</DT>
