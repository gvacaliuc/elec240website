
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 2.3
</h2>
<h2>
Optoelectrical Signal Sources and Sinks
</h2>
</center>
<p>
    Since we will be building an optical communication system, we will need some devices for converting electrical signals to and from light, as well as to and
    from sound. We will look at two: the photodiode, which converts light into an electrical signal, and the light emitting diode (LED) which converts electric
    current to light.
</p>
<h3>
    Equipment
</h3>
<ul>
<li>Photodiode
<li>Red LED
</ul>
<h3>
    Part A: The Photodiode
</h3>
<p>
    - Connect the short lead (cathode) of the <a href=/misc_images/#photo-diode>photodiode</a> to
    ground and the long lead (anode) to CH1 of the scope. You can use the BNC clip leads for this, but the better way (which leaves your hands free) is to the
    plug it into the breadboard and wire it to the appropriate interface pins (pin 1 to anode, pin 14 to cathode).
    <br/>
    <img
        border="0"
        width="320"
        height="240"
        src="../figs/photo2.3.1a1.jpg"
    />
</p>
<p>
- View the DC signal on the scope.    <strong>Note the voltage produced by photodiode. How does it change when you cover the photodiode with your hand?</strong>
</p>
<p>
    - Set CH1 to AC. What are the amplitude and frequency of the signal?
</p>
<DT>
<DD><p>
    o Hint: Click on the ruler by the bottom left corner of the oscilloscope view for helpful measurement tools.
</p></DD>
<p>
    - Explain the waveform you observed in the previous step. Switch back to DC.
</p>
<h3>
    Part B: Light Emitting Diode
</h3>
<p>
    - Using a 220-ohm (red-red-brown) resistor and your <a href=/misc_images/#red-led>red LED</a>, wire the following circuit:
    <br/>
    <img
        border="0"
        width="315"
        height="122"
        src="../figs/img159.png"/>
</p>
<p>
    - First wire the resistor and LED on the breadboard. There are two ways to connect the power supply to the circuit (use one or the other MISSINGDATA not both):
</p>
<DD><p>
    o The first way: Plug your <a href=/misc_images/#banana-adapter>BNC-banana adapter</a> into the 6V
    power supply terminals. Note: There is a bump on one side of the adapter to denote which prong is connected to ground. Be sure to plug this prong into the
    black terminal of the power supply.
    <br/>
    <center>
    <img
        border="0"
        width="300"
        height="400"
        src="../figs/dc_bnc.jpg"/>
    </center>
</p>
<p>
    Then use the clip leads to connect to the LED and resistor.
    <br/>
    <center>
    <img
        border="0"
        width="350"
        height="305"
        src="../figs/photo2.3.2c1.jpg"/>
    </center>
</p></DD>
<DD><p>
    o The other way: Use the BNC adapter as above, but use a BNC patch cord to connect the power supply to J1-3. Use two pieces of wire to connect ground (pin
    14) to the LED and J1-3 (pin 3) to the resistor.
    <br/>
    <br/>
</p></DD>
<p>
    - Turn on the power supply. Slowly increase the voltage until you see the LED just begin to glow. Measure the voltage across the LED. If the LED doesn't
    light by the time the meter on the power supply reads 3 V, check your circuit to make sure the diode is wired in the correct orientation. Unlike a resistor
    or light bulb, the LED is <em>polarized.</em> The anode must be positive for it to glow. Reverse the LED and verify that this is the case.
</p>
<p>
    - Set the supply voltage to 3, 4, and 5 volts. At each step note the brightness of the LED and the voltage across it.
</p>
<p>
    - Next power the LED with the FGEN instead of the power supply. Set it to produce a 100 Hz square wave with minimum amplitude.
</p>
<p>
    - Increase the amplitude until it begins to glow. Is the glow steady?
</p>
<p>
    - Slowly reduce the frequency of the FGEN. <strong>At what frequency does noticeable flicker begin?</strong>
</p>
<p>
    - <strong>How does the number you measured in the previous step relate to the frame rate of television and motion pictures?</strong>
</p>
<h3>
    Part C: Optical Communication
</h3>
<p>
    - Now connect the photodiode to CH1 of the scope using a BNC-to clip leads cord.
    <br/>
    <center>
    <img
        border="0"
        width="320"
        height="240"
        src="../figs/photo2.3.3a.jpg"/>
    </center>
</p>
<p>
    - With the LED still connected to the FGEN as in the previous part, set the frequency to 100 Hz.
</p>
<p>
    - Hold the photodiode (pointing down) above the LED (pointing up). Adjust their relative positions to maximize the signal displayed on the scope.
</p>
<DD><p>
    o It may help to shield the components from ambient light with your hand.
</p></DD>
<p>
    - <strong>Describe the waveform. Is it what you would expect?</strong>
</p>
<p>
    - Set the FGEN to produce a triangle wave. Take a screenshot of the waveform. <strong>Is it what you expected?</strong>
</p>
<p>
    - Reset the FGEN to produce a square wave. <strong>What is the maximum distance over which you can transmit a recognizable signal?</strong>
</p>
<DD><p>
    o Hint: Switch to AC signal with higher gain.
</p></DD>
<p>
- We have several of the components needed for building an optical communication system.    <strong>What components are missing? What problems remain to be solved?</strong>
</p>
