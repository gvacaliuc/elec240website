
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 1.1
</h2>
<h2>
DC Measurements: the DMM
</h2>
</center>
<h3>Equipment</h3>
<ul>
<li><a href=/misc_images/#batt-pack>Battery Pack and Batteries</a>
<li><a href=/misc_images/#lamp-board>Lightbulb Socket Board</a>
<li> Digital Multimeter
<li> Banana Plug Patch Cords
</ul>
<h3>
    Part A: Measuring Voltage with the DMM
</h3>
<DL>
<p>
    - Turn on the digital multimeter (DMM) to the setting for DC volts measurement:
</p>
<p>
<img
        width="319"
        height="400"
        src="../figs/fluke73a.jpg">
</p>
<p>
    - Make sure the negative (black) lead is plugged into the COM terminal and the positive (red) lead is plugged into the V terminal, as shown in the picture.
    COM stands for common, or in other words, the termin al that is the point of reference for other terminals.
</p>
<p>
    - <strong>Measure the voltage of each battery</strong> by holding the positive probe against the top of the battery and the negative probe against the
    bottom.
</p>
<DD><p>
    o Note: In measuring voltage, we are always measuring the <em>difference in potential </em>between two nodes. So the meter is always connected across two
    points.
</p></DD>
<p>
- Place the two batteries into the holder in the orientation indicated.    <strong>Measure the voltage of the battery pack. It should be equal to the sum of the two batteries. Is it?</strong>
</p>
<DD><p>
    o
    <em>
        Caution: Be careful not to short the two leads of the battery pack together once the batteries are installed. To be safe, remove at least one of the
        batteries when the pack is not in use.
    </em>
</p></DD>
<p>
- Wire the circuit below by screwing the leads from the battery pack to L and R terminals of the lamp board. The bulb should light (though rather dimly).    <strong>Measure the battery voltage again. Is it the same as before?</strong>
    <br/>
    <img src="../figs/img152.png"/>
</p>
<p>
    <h3>Part B: Measuring Current with the DMM</h3>
</p>
<p>
To measure current, we must connect the meter <em>in series</em> with the circuit we are measuring, as in the figure below. This is because current flows    <em>through</em> a conductor, whereas voltage appears <em>across</em> two conductors.
</p>
<p>
    This is because current flows <em>through</em> a conductor, whereas voltage appears <em>across</em> pairs of conductors.
</p>
<p>
    <img src="../figs/img153.png"/>
</p>

<p>
    - With the meter disconnected from the circuit, set the function switch to DC current ("A" with straight solid and dashed lines above it). Move the red meter lead to the 300 mA terminal.
</p>
<DD><p>
    o
    <em>
        Caution: An ammeter must always be connected in series. Connecting an ammeter in parallel with a circuit element can pass very large currents through
        the ammeter, blowing its internal fuse or damaging it. A good practice is to always reset the DMM to voltage measurement settings after making a
        current measurement.
    </em>
</p></DD>
<p>
    - Use the NC ('not connected') terminal as a node to connect the positive battery terminal to the positive lead of the DMM.
</p>
<p>
    - <strong>Note the current value displayed on the DMM.</strong>
</p>
<p>
    <h3>Part C: Measuring Resistance with the DMM</h3>
</p>
<p>
    - Set the DMM to Ohms (W) and return the positive meter lead to Volts/Ohms terminal. Touch the two probes together. The meter should read zero resistance.
    If it reads more than a few tenths of an ohm, check for poor connections or have your meter serviced.
</p>
<p>
- Select several resistors at random from your parts kit. For each resistor, determine its nominal value from the    <a href=/references/color_code>color code</a>, then measure its resistance by touching one probe to each lead of the
    resistor. <strong>Do the nominal and measured values agree?</strong>
</p>
<DD><p>
    o To read a 4-band resistor color code, view it with the gold/silver band to the right. The first two band colors correspond to the first two digits of the
    resistor value and the third band color is the multiplier. The fourth band is the percent tolerance. Tolerance means that the actual resistance value is
    guaranteed to be within the marked value specified percent.
</p></DD>
<DD><p>
    o To measure resistance, lay the resistor on the bench and test as shown below.
    <br/>
    <img src="../figs/res_meas1.jpg"/>
</p></DD>
<DD><p>
    o
    <strong>
        What's wrong with holding the leads and probes between your fingers?
        <br/>
    </strong>
    <img src="../figs/res_meas2.jpg"/>
</p></DD>
<p>
- The actual resistance R of a resistor having nominal values R<sub>0</sub> and tolerance d lies in the range R<sub>0</sub>(1+d).    <strong>What is the tolerance of a series connection of two such resistors? Of a parallel connection?</strong>
</p>
<p>
    - Obtain ten resistors with the same marked value. Measure the resistance of each resistor. <strong>Does your batch have the stated accuracy?</strong>
</p>
<p>
    - Holding one DMM lead in each hand, measure your own resistance. The reading may be unstable, therefore the resolution is limited to the digit that
    changes least often. <strong>What is the value and resolution of your resistance?</strong>
</p>
<p>
    -
    <strong>
        Does your resistance change when you wet your fingers? If so, speculate why. What voltage would be necessary to produce a 5mA current through you?
    </strong>
    (Why 5mA? Read <a href=../safety>Safety</a>).<strong></strong>
</p>
<p>
    - Using the DMM,
    <strong>
        measure the resistance of the light bulb. Does this correspond to the value you would expect from Ohm's Law given the values of voltage and current you
        measured in Parts A and B?
    </strong>
</p>
<DD><p>
    o
    <em>
        Caution: The DMM can only measure the resistance of an element when it is disconnected from the circuit. Remember to turn off the power source or the
        value measured will be inaccurate.<strong></strong>
    </em>
</p></DD>
<p>
    <h3>Part D: Measuring the I-V Characteristics of the Light Bulb</h3>
</p>
<p>
    An ideal resistor obeys Ohm's law: I=V/R, i.e. the current through the element is proportional to the voltage across it. But for most real materials, the
    resistance changes as the temperature changes, and clearly, the temperature of the light bulb's filament increases as more current flows through it. Let's
    find out how the current and voltage of our light bulb are related.
</p>
<p>
    For this measurement, we will need to vary the voltage applied to the bulb, so we will need a variable voltage source. This is provided by the DC Power
    Supply on the VirtualBench. The DC power supply actually contains two variable voltage sources, but we will be using only one of them, the 0-6V supply.
</p>
<p>
    - Make sure the DC power dongle is attached to your VirtualBench (VB).
    <br/>
    <img src="../figs/dongle_label.jpg"/>
</p>
<p>
    - Set the DMM to DC Volts. Connect the black (-) probe to the black 0-6V output terminal and the red (+) probe to the red terminal.
</p>
<p>
    - Press the power button on the power supply interface below the oscilloscope screen. Gradually increase the output voltage by raising the voltage in the
    +6V setting. Both the power supply and the DMM should show increasing voltage values. For several different values, note both the power supply +6V setting
    and the DMM reading. <strong>How do the two compare? </strong>Return the voltage output to zero.
</p>
<DD><p>
    o
    <em>
        Note: For the rest of this part, you will need to use VirtualBench as your second DMM. To use the DMM feature of VirtualBench, plug in the leads to the
        digital multimeter feature of VirtualBench. Note that VirtualBench contains two pairs of sockets for the leads: the left socket pair can be used for
        measuring voltage and resistance, while the right socket pair can be used for measuring current.
        <br/>
        <img src="../figs/img199.png"/>
    </em>
</p></DD>
<p>
    - Wire the circuit below. You will need <a href="http://www.ece.rice.edu/~dpr2/elec240labs/elec_food.jpg">banana plug patch cords</a> for this.
    <br/>
    <img src="../figs/img154.png"/>
</p>
<p>
    - Measure the current for voltages between 0 V and 1 V, in steps of about 0.2 V. and between 1 V and 5 V in steps of about 0.5 V. It is not necessary to
    have V exactly equal to 1.000, 1.500, etc. Just get it close and write down the numbers accurately.
</p>
<p>
    - <strong>Plot I as a function of V. <a name="How?"></a><a href=../file.8>How?</a> </strong>
</p>
<p>
    - <strong>To what point on this curve does the value of resistance you measured with the ohmmeter correspond?</strong>
</p>
<p>
- Now generate a I vs. V curve for a 1000-ohm resistor (brown-black-red). You can use the NC and L binding posts to hold the resistor for this measurement.    <strong>Is our assumption that I=V/R for all V a valid one?</strong>
</p>
<p>
    - When finished, turn off the DMM.
</p>
</DL>
