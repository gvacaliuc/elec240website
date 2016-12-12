
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 3.1
</h2>
<h2>
Resistive Voltage Dividers
</h2></center>
<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>Resistors
<li>1-k&#8486; Potentiometer
</ul>
<p>
    <a href=/misc_images/#bnc-t>BNC T Connector</a>
</p>
<h3>
    Part A: Measuring AC Voltage with the DMM
</h3>
<p>
    - Connect the BNC T-connector to CH1 of the scope.
</p>
<p>
    - Use a BNC patch cord to connect one end of the T to the <tt>FGEN</tt> output. Connect a BNC clip lead to the other end of the T.
    <br/>
    <img
        border="0"
        width="350"
        height="288"
        src="../figs/img200.png"/>
</p>
<p>
    - Set the <tt>FGEN</tt> to produce a 2-V peak-to-peak, 100Hz sine wave.
</p>
<p>
    - Set the DMM to AC Volts and connect the probes to the clip leads.<strong> What is the voltage reading on the DMM?</strong>
</p>
<p>
    - Set the <tt>FGEN</tt> to produce a square wave. What is the voltage reading on the DMM?
</p>
<p>
    - Reset the <tt>FGEN</tt> to sine wave. Note the reading on the DMM at 5 Hz, 50 Hz, 500 Hz, 5 kHz, and 50 kHz.
</p>
<p>
    - <strong>What is the useful frequency range of the DMM for measuring AC signals?</strong>
</p>
<DT>
<DD><p>
    o The AC voltage function of the DMM is calibrated to read (approximately) the <em>RMS</em> value of the waveform. RMS stands for root-mean-square i.e. the
    square root of the mean value of the square of the function:
    <br/>
    <strong>
        <img border="0" width="185" height="62" src="../figs/rmseqn.png"/>
    </strong>
</p></DD>
<DD><p>
o We'll see the importance of this when we study power. For now just remember that for a sine wave, V<sub>RMS</sub> = 0.707 V<sub>peak</sub>.    <strong></strong>
</p></DD>
<h3>
    Part B: The Basic Voltage Divider
</h3>
<p>
    - Wire the following circuit using 10k&#8486; (brown-black-orange) resistors for both R<sub>1</sub> and R<sub>2</sub>:
    <br/>
    <strong>
        <img border="0" width="348" height="151" src="../figs/img162.png"/>
    </strong>
</p>
<p>
    - <strong>What should the voltage divider ratio (v<sub>out</sub>/v<sub>s</sub>) be? </strong>
</p>
<p>
    - Set the <tt>FGEN</tt> to produce a 2 V p-p sine wave.<strong></strong>
</p>
<p>
    - <strong>Measure v<sub>out</sub> with the oscilloscope. Is it what you expect?</strong>
</p>
<p>
    - Change R<sub>1</sub> and R<sub>2</sub> to 47&#8486; (yellow-violet-black). <strong>What is the output voltage?</strong>
</p>
<p>
    - Now change R<sub>1</sub> and R<sub>2</sub> to 1M&#8486;. <strong>What is the output voltage?</strong>
</p>
<DD><p>
    o No circuit exists in isolation. To be useful its input or output (or both) should be connected to some other circuit. Unfortunately the interaction
    between the circuit and a non-ideal source or load causes it to behave differently than it would in an idealized situation. With careful design, this
    interaction can be minimized or accounted for. If ignored it can reduce the performance of the system, or keep it from working altogether.<strong></strong>
</p></DD>
<p>
    - A more accurate model of the system we measured would be:
    <br/>
    <strong>
        <img border="0" width="369" height="95" src="../figs/img163.png"/>
    </strong>
</p>
<p>
- Based on your measurements,    <strong>what are the output resistance (R<sub>S</sub>) of the function generator and the input resistance (R<sub>L</sub>) of the scope?</strong>
</p>
<h3>
    Part C: The Potentiometer
</h3>
<p>
    - A potentiometer (pot for short) is a fixed value resistor with a third, movable contact or <em>slider </em>which may be positioned anywhere along the
    resistive element. If we represent the position of the slider by &#945;, where &#945; varies between 0 (fully counterclockwise) and 1 (fully clockwise), then the
    resistance between the lower end of the resistor and the slider will be &#945;R and between the slider and the upper end will be (1-&#945;)R, where R is the total
    resistance of the potentiometer.
</p>
<p>
    - If we connect the two fixed contacts to a voltage source and measure the output between the movable contact and one fixed contact, we get a variable
    voltage divider:
    <br/>
    <img border="0" width="521" height="143" src="../figs/img164.png"/>
</p>
<p>
    - Then the output is:
    <br/>
    <img border="0" width="352" height="48" src="../figs/poteqn.png"/>
</p>
<p>
    - Select a 10k&#8486;. It will have three short wires sticking out in a triangular pattern. The center terminal is the slider contact and the two outer terminals
    are the fixed contacts.
    <br/>
    <img border="0" width="377" height="196" src="../figs/pots.jpg"/>
</p>
<DD><p>
    o
    <em>
        Note: Figuring out the value of a pot can be tricky. Some pots are labeled directly with the value (e.g. "100" or "10K"). Others are labeled using the
        same code as for fixed resistors, except that numbers, rather than colors, are used. For example, a 10k&#8486; resistor would have the bands
        brown-black-orange. The values of these colors are 1, 0, and 3, so a 10k&#8486; pot would have the label "103".
    </em>
</p></DD>
<p>
    - Wire the following circuit:
    <br/>
    <img border="0" width="366" height="121" src="../figs/img165.png"/>
</p>
<p>
    - Set the function generator to produce a 2 V p-p 100-Hz sine wave.
</p>
<p>
    - Set the potentiometer adjustment screw to midscale and <strong>measure v<sub>out</sub>.</strong>
</p>
<p>
    - The pot has a scale divided into 10 equal divisions, presumably representing 10 equal divisions of resistance. Set the pot to each of these 10 divisions
    and measure v<sub>out</sub>. <strong>Is this presumption correct?</strong>
</p>
<h3>
    Part D: Thevenin Equivalent Circuit of a Microphone
</h3>
<p>
    - Recall that the Thevenin theory states that any DC circuit can be modeled as a power source and resistance. If a known resistive load is attached to a
'blackbox' circuit, such as an unknown power supply, the Thevenin equivalence can be found for this blackbox circuit.    <strong>How do you find the Thevenin equivalent circuit?</strong>
</p>
<p>
    - Another advantage of knowing the Thevenin equivalence of a blackbox circuit is that we can determine a load resistance that maximizes the power transfer
    to the load. <strong>What should the load resistance be for maximum power transfer?</strong>
</p>
<DD><p>
    o Note: Thevenin theory not only applies to power supplies and function generators, but also to sensors. When sensors detect signals and provide some
    outputs, they can be considered as sources with dependent voltage or current supplies.
</p></DD>
<DD><p>
    o Recall that a speaker produces sound by converting current flowing through the voice coil into mechanical motion of the speaker cone. By reversing this
    process, it is also possible to use a speaker as a microphone. Sound waves will cause the speaker cone and voice coil to move. As the voice coil moves
    through the permanent magnet, a current is induced in the voice coil and a voltage appears across the voice coil.
</p></DD>
<p>
    - Two speakers will be used here as a pair. One of them is the speaker, converting the sine wave generated from function generator to sound. The other
    plays the role of a microphone, and reverses the sound to electrical waves. They are connected as below.  
    <br/>
    <img border="0" width="273" height="273" src="../figs/img201.png"/>
</p>
<p>
    - Now the two wires connected to the microphone (the upper speaker) can be considered as the two terminals of the load resistance. The whole system
    consisting of the function generator, the speaker and the microphone should be seen as a circuit with a sine wave power supply (Thevenin voltage) and an
    internal resistance (Thevenin resistance).
</p>
<p>
- Set the <tt>FGEN</tt> to generate a sinusoid within audible range and connect the upper speaker (microphone) to the oscilloscope.    <strong>Measure the peak-to-peak amplitude, which will be the Thevenin voltage.</strong>
</p>
<p>
    - Connect different resistances between 1 and 10 ohms to the output of the microphone and measure the load voltage V<sub>L</sub> of these resistances.
</p>
<p>
    -
    <strong>
        Calculate the Thevenin resistance of the system for each load and the power transferred to each load resistance. What is the average Thevenin
        resistance and is there any significant variation between measurements?
    </strong>
</p>
<p>
    - <strong>Draw the power vs. resistance diagram</strong> and find the maximum point.
</p>
<p>
    <strong> </strong>
</p>
</DT>
