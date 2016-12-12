
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 2.1
</h2>
<h2>
Electroacoustic Transducers I
</h2>
</center>
<p>
    In this section we will discover different ways to detect and change a signal.
</p>
<h3>Equipment</h3>
<ul>
<li><a href=/misc_images/#bnc-cliplead>BNC Male to Clips test lead</a>
<li><a href=/misc_images/#vb-probe>Oscilloscope probe</a>
</ul>
<h3>
    Part A: Listening to a Signal
</h3>
<p>
    - Set up the function generator to produce a 1-kHz sine wave with a peak-to-peak (p-p) amplitude of 5 Volts. Verify settings by viewing on the
    oscilloscope.
</p>
<p>
    - Using the BNC-to-clip test lead, connect the output of the function generator to the speaker leads. <strong>What do you hear?</strong>
</p>
<p>
    - With the speaker still connected to the FGEN, measure the amplitude of the voltage across the speaker. This time, connect an oscilloscope probe to one of
the speaker leads. (The ground lead can remain disconnected because it is already internally connected to the FGEN ground).    <strong>What is the peak-to-peak measurement now? Why did it change?</strong>
</p>
<p>
- Using FGEN controls, vary the amplitude, frequency, and shape of the signal.    <strong>How does the nature of the sound change as these signal parameters change?</strong>
</p>
<p>
    - Disconnect the speaker.
</p>
<h3>
    Part B: Thevenin Equivalent and Maximum Power Transfer
</h3>
<p>
    Looking back at the diagram in the Background section we can see what caused the reduction in signal amplitude (attenuation): R<sub>out</sub> of the
    function generator and R<sub>L</sub> of the speaker form a voltage divider. To reduce the attenuation, one possibility is to either reduce R<sub>out</sub>
    or increase R<sub>L</sub>. For this, the first step would be to determine what R<sub>out</sub> is.
</p>
<p>
    - Assuming that the oscilloscope provides infinite load, <strong>determine the Thevenin voltage</strong> (use same FGEN settings as in Part A).
</p>
<p>
- Referring to the Background section, <strong>calculate the Thevenin resistance</strong> for various R<sub>L</sub>: 20, 30, 50, 100 Ohms.    <strong>Does the Thevenin resistance vary?</strong>
</p>
<p>
    - <strong>Calculate the average power</strong> dissipated by each load.
</p>
<DT>
<DD><p>
    o The amount of average power dissipated by the load is another way of stating the amount of average power delivered to the load.
</p></DD>
<DD><p>
    o P<sub>avg</sub>=0.5*(V<sub>m</sub><sup>2</sup>/R<sub>L</sub>) where V<sub>m</sub> is the maximum amplitude of voltage across R<sub>L</sub>.
</p></DD>
<p>
    Maximum Power Transfer: The maximum power transfer theorem states that the maximum power is delivered to the load when the load resistance is equal to the
    Thevenin resistance of the source. This is important in applications such as when the load is a cell phone antenna and you need maximum power delivered to
    improve coverage area; another example is the load being an audio speaker that requires maximum power to deliver the highest sound level.
</p>
<p>
    - <strong>Make a graph of P<sub>avg</sub> vs. R<sub>L</sub></strong> and show how the maximum power transfer theorem is verified by these results.
</p>
