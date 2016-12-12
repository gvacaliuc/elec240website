
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 5.2
</h2>
<h2>
Frequency Response
</h2>
</center>
<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>    Integrator from last experiment
<li>    1k&#8486; and 100&#8486; resistors
<li> Lab computer or laptop

</ul>
<h3>
    Part A: Measuring Frequency Response
</h3>
<p>
   In this part of the lab you will use look at the frequency response of your integrator.
</p>
<p>
    - Disconnect the input and output from your integrator and modify it as shown below. For the input, connect a 1 Vp-p  sinusoidal signal from your VirtualBench function generator.
    <br/>
    <img width="559" height="391" src="../figs/spiceintegrator.png"/>
    <br/>
    <br/>
</p>
<p>
- Record output peak-to-peak voltage values for the following frequencies: 10Hz, 100Hz, 500 Hz, 800 Hz, 1kHz, 1.5kHz, 2kHz, 5kHz, 10kHz, 50kHz.</p>
<p>
- Calculate the gain in decibels (dB) for your circuit at each of these frequencies.
</p>
<DT>
<DD><p>
o $Gain (dB) = 20*log10(\frac{Vout}{Vin})$
</p></DD>
<p>
- Plot $Gain(dB)$ vs. $Frequency (Hz)$ in Matlab.
- At what frequency does the gain begin to drop?
<DD>o	<strong> Does the cutoff frequency, $f_c$ roughly equal $\frac{1}{2*\pi*R5*C2}$?</strong>  </DD>
</p>
<p>
<h3>
    Part B: Circuit Simulation
</h3>
<p>The remainder of the lab can be done from a computer (lab computer or personal laptop). We will be using circuit simulation software called LTSpice. Spice stands for (Simulation Program with Integrated Circuit Emphasis). </p>
<p>- Download LTspice from linear.com.  There are Windows and Mac versions available.  Please note that the instructions below are specifically for Windows. </p>
<p>- Click on New Schematic and create the same circuit you built on your breadboard shown above.</p>
<DD><p>o	Place components by going to the Edit menu or shortcut buttons.</p></DD>
<DD><p>o	The opamp is found under Edit->Components->[OpAmps]->opamp. The voltage source is found under Edit->Components->voltage. Connect components using Edit->Wire (or the shortcut button F3).</p></DD>
<DD><p>o	Other convenient shortcuts are:</p></DD>
<ul><li><DD> Ctrl-R for Rotate</p></DD>
<li><DD> Delete, or F5 for Delete</p></DD>
<li><DD> F6 for Copy</p></DD>
<li><DD> F7 for Move</p></DD>
<li><DD> F8 for Drag</p></DD>
<li><DD> Esc to exit out of a mode</p></DD></ul>
<DD><p>o	The component opamp is just a symbol of an opamp and in order for Spice to see the model, you need to place a Spice Directive calling the location: Edit->Spice Directive. Then enter .lib opamp.sub</p></DD>
<DD><p>o	Set the voltage source  to AC by right-clicking it and selecting Advanced. Set AC amplitude to 1.</p></DD>
<DD><p>o	Enter in R and C values by right-clicking these components.</p></DD>
<p>o	Optional MISSINGDATA label nets (i.e., wires) by right-clicking on nets.</p>
<p>-	Perform an AC analysis. An AC analysis will evaluate the gain (Vout/Vin) and phase over a specified range of frequencies and plot it.</p>
<DD><p>o	Click on the Running Man icon and select AC analysis (or go to Simulate->Run).</p></DD>
<DD><p>o	Use a decade frequency sweep with at least 10 points per decade over the range of 1 Hz to 10 MHz. This will appear as a Spice directive on your schematic as </p></DD>
<DD><p>.ac dec 10 1 10meg</p></DD>
<DD><p>o	Click on the Vout node for gain and phase plots to appear. You will notice that the gain is displayed in dB and phase in degrees. The x-axis will be logarithmic, i.e., the step size is $10n$, where $n$ is a non-negative integer.  Each of the steps is called a decade (dec).</p></DD>
<p>- <strong>Take a screenshot of your plots.</p></strong></DD>
<p>	- <strong>What is the gain at low frequencies? What is the cutoff frequency? What is the slope of the gain with respect to frequency for high frequencies (express in terms of dB/dec)? Do these values match what you measured on your breadboard?</strong></p></DD>
<p>	- <strong>What is the phase for very low frequencies? At 0dB? And for very high frequencies? Can you explain why?</strong></p></DD>

</DT>
