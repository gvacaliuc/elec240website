
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 5.1
</h2>
<h2>
Function Generator
</h2>
</center>
<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>    LM741 (4x)
<li>    Resistors according to your design
<li>    Capacitors according to your design
</ul>
<h3>
    Part A: Build a Function Generator
</h3>
<p>
    In this lab experiment, we will be building our own function generator using two new types of op amp circuits.
</p>
<p>
    - Wire up the following RC relaxation oscillator circuit (see Introduction to read about its functionality):
    <br/>
    <img width="559" height="391" src="../figs/multivib.png"/>
    <br/>
    <br/>
</p>
<p>
    - <strong>Is the output as expected? Provide a screenshot in your report.</strong>
</p>
<p>
    - <strong>What is the frequency of oscillation? </strong>
</p>
<p>
    o The frequency should be equal to $f = \frac{1}{2.2*R1*C1}$. Is this what you measure?<strong></strong>
</p>
<p>
    - <strong>Does the frequency change as expected when R1 is changed?</strong>
</p>
<p>
    - Cascade an integrator circuit to the output as shown below:
    <br/>
    <img width="580" height="264" src="../figs/integrator.png"/>
    <strong></strong>
</p>
<p>
    - <strong>Is the integrator working as expected? Explain and provide a screenshot.</strong>
</p>
<p>
    - Measure the DC offset of Vout2. <strong></strong>
</p>
<p>
    o <em>Note: DC offset is the average voltage of your waveform.<strong></strong></em>
</p>
<p>
- Eliminate the DC offset by placing a DC blocking capacitor (any capacitor between 0.1uF and 1uF) in between the RC relaxation oscillator and integrator.    <strong>Provide a screenshot.</strong>
</p>
<p>
    - Now add on to your circuit so that it also generates a sinusoid. <strong>Provide a screenshot.</strong>
</p>
<p>
    - Build a gain stage to your circuit to modulate the amplitude of your sinusoidal output.<strong></strong>
</p>
</DT>
