
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 1.2
</h2>
<h2>
The Oscilloscope and Function Generator
</h2>
</center>
<h3>Equipment</h3>
<ul>
<li> BNC Patch Cords
</ul>
<p>
    So far we've measured only constant (or nearly constant) voltages and currents. A much more interesting class of signals are <em>time varying</em> voltages and currents. For a slowly time varying signal, we could just write down the values as they change (as we did in plotting the light bulb I-V curve), but
    for most time varying signals we need something a bit faster. On the VirtualBench, that would be the <em>oscilloscope</em>.
</p>
<p>
    In order to measure time varying signals, we need a source of time varying signals. The DC power supply on the VirtualBench is our source of constant voltages, and the <em>function generator</em> is our source for that class of time varying signals known as <em>periodic signals</em>.
</p>
<h3>
    Part A: Viewing Signals with the Oscilloscope
</h3>
<DL>
<p>
    First get acquainted with the settings of the oscilloscope, even though you will continue using many of them in their default setting. Make sure you are being consistent in using either CH 1 or 2.
</p>
<p>
    - Make sure the oscilloscope controls are as follows:
</p>
<DD><p>
    o Time/Div: 1ms
</p><DD>
<DD><p>
    o Mode: Auto
</p></DD>
<DD><p>
    o Display: CH 1
</p></DD>
<DD><p>
    o Volts/Div: 2V
</p></DD>
<DD><p>
    o AC-DC: DC
</p></DD>
<DD><p>
    o Trigger: Edge; CH 1; Rising
    <br/>
    <img src="../figs/vb_oscilloscope_labels.jpg"/>
</p></DD>
<p>
    - If everything is in order, you should see a red horizontal line through the middle of the screen.
</p>
<p>
    - Set up the function generator to produce a 1kHz sine wave (found to the right of the oscilloscope display). Turn on the power button for the function
    generator. Set it as follows:
</p>
<DD><p>
    o Frequency: 1.0 kHz
</p></DD>
<DD><p>
    o Amplitude 3 Vpp (Volts, peak-to-peak)
</p></DD>
<DD><p>
    o DC Offset: 0 V
</p></DD>
<DD><p>
    o Duty Cycle (only used for square wave setting)
</p></DD>
<DD><p>
    o Function: Sine wave
</p></DD>
<p>
    - Connect the function generator's OUTPUT to the oscilloscope's CH 1 input. The easiest way to do this is to connect one end of a BNC patch cord to the
    function generator FGEN and the other to the oscilloscope CH 1. This connects the generator's ground and signal terminals to the scope's ground and terminals. If all has gone well, you should see 6 full cycles of a sine wave in red.
</p>
<p>
    - Now examine the effect of each control:
</p>
<DD><p>
    o Move the display with the positioning controls - click and drag the toolbar at the top.
</p></DD>
<DD><p>
    o Change the Time/Div and Volts/Div settings to see what effects are produced.
</p></DD>
<DD><p>
    o Click on the ruler in the bottom left of the screen and change the settings of the function generator to observe how the oscilloscope automatically
    measures signal features such as frequency, period, and amplitude.
</p></DD>
<DD><p>
    o <strong>Why do you think these numbers are slightly different from the function generator settings?</strong>
</p></DD>
<p>
    - Examine the various waveforms produced by the function generator. Examine the effects of the DUTY CYCLE and DC OFFSET controls. Before going on, be certain that you are comfortable with the oscilloscope and function generator. If you are having problems, ask your labbie for help.
</p>
<h3>
    Part B: Quantitative Measurements with the Oscilloscope
</h3>
<p>
    In addition to allowing us to view the "shape" of a signal, the oscilloscope can also measure voltage, amplitude, time intervals, and frequency.
</p>
<p>
- Connect the oscilloscope CH 2 input to the 0-6V output of the DC power supply. For this you can use a BNC patch cord and your <a name="BNC"></a>    <a href=/misc_images/#banana-adapter>BNC to banana plug adapter</a>.
    <br/>
    <img src="../figs/dc_bnc.jpg"/>
</p>
<p>
    - Switch to CH 2 and under Channel Settings, set the vertical offset to 0. This effectively sets the reference to 0, known as "zeroing" the signal.
</p>
<p>
    - Increase the voltage to 2V. Continue to increase the voltage and see how well the scope readings and power supply settings agree.
</p>
<p>
    - <strong>Why would we want to use the oscilloscope to measure a "DC" voltage? </strong>
</p>
<p>
    - Switch to CH 1 and "zero" Channel 1 as above. Set the function generator to produce a 2kHz sine wave. Set the TIME/DIV setting to 100 &mu;s. Measure the distance between two successive zero crossings of the same slope and multiply by the Time/Div factor to get the <em>period</em> of the waveform. Using the formula f=1/T, determine the measured frequency of the signal. <strong>How does this compare with the nominal frequency? </strong>
</p>
<DD><p>
    o There are several ways we can express the amplitude of a signal. For the sine wave y(t)=Asin(2&pi;ft) the amplitude A is equal to the distance from the positive (or negative) peaks of the waveform to the t-axis. This peak amplitude measurement is equally useful for any waveform which has equal positive and
    negative peaks.
</p></DD>
<DD><p>
    o Arbitrary waveforms may not have this property, so a more general measurement is the peak-to-peak amplitude, the distance between the positive and negative peaks of the signal.
</p></DD>
<DD><p>
    o Other measures of a signal's magnitude include average and rms, which we'll talk about later. Since in general these different measures have different values, it is a good idea always to specify which amplitude measurement you are using.
</p></DD>
<p>
    - We can also use the oscilloscope to measure the <em>amplitude </em>of a signal. Disconnect your oscilloscope from the function generator and use a BNC clip lead to connect CH 1 to the square wave and ground outputs of the scope, located to the right of the CH 2 input socket.
</p>
<p>
    - <strong>Sketch this signal's waveform.</strong> What is its period? What is its frequency? Adjust the CH 1 Volts/Div switch so that the waveform nearly
    fills the screen vertically. Measure the peak-to-peak amplitude by counting the number of divisions between the upper and lower peaks and multiplying by the Volts/Div factor. Does your measurement of the waveform's amplitude correspond to the VB's measurement? (Click on the ruler button to look at the signal's measurements.)
</p>
<p>
    - <strong>Take a screenshot of the waveform</strong> by going to File-&gt;Export Screenshot
</p>
