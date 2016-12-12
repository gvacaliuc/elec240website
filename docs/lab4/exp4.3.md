
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 4.3
</h2>
<h2>
Transducer Amplifiers
</h2>

</center>
<h3>

<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>741 Op Amp
<li>10 k&#8486; Resistors
<li>100 k&#8486; Resistors
<li>Other resistors according to your design
<li> 0.1 &#181;F Capacitor
<li> Dynamic microphone
<li> Telephone handset
</ul>
<p>
    In Lab 2 we saw that our input transducers (microphone and photodiode) produced signals of only a few millivolts, while our output transducers (speaker and
    LED) required signals of a few volts. To make up this discrepancy, we need to amplify the signal levels produced by the input transducers.
</p>
<h3>
    Part A: Photodiode Amplifier
</h3>
<p>
    The inverting op-amp circuit works by taking the current that flows into the "virtual ground" at the inverting input and forcing it to flow in the feedback
    resistor. Since the voltage across R<sub>F</sub> is equal to R<sub>F</sub>I<sub>F</sub>, the output voltage (on the other terminal of R<sub>F</sub> is
    proportional to the current flowing into the virtual ground. What if instead of this current originating from the voltage across R<sub>1</sub>, it instead
came directly from a current source? Well, the output voltage would still be proportional to it: <em>v</em><sub>out</sub>=-R<sub>F</sub>I<sub>F</sub>=-R<sub>F</sub>I<sub>in</sub>, i.e., we have an amplifier which accepts a current as an input and produces a voltage as an output. This is called a    <em>transresistance amplifier</em>. (Since a resistance converts its current to a voltage (v=R*i), a transresistance converts a current in one part of the circuit to a voltage in another.)
</p>
<p>
    In Lab 2 we measured the <em>voltage</em> across the photodiode and found some fairly distorted waveforms. It turns out that the <em>current</em> produced
    by a photodiode is proportional to the intensity of the light falling on it, while the voltage is proportional to the <em>logarithm</em> of the intensity,
    hence the distortion. If we could produce an output signal proportional to the photodiode current, we would have a much better transducer.
</p>
<p>
    - Wire the following circuit. (You can modify the previous circuit by removing the 10 k&#8486; resistor and replacing it with the photodiode (connected
    to ground rather than to the function generator)).
    <br/>
    <img width="306" height="177" src="../figs/img176.png"/>
</p>
<p>
    - As you did in Lab 2, note the output voltage, v<sub>out</sub>, and observe how it changes as you cover and uncover the photodiode with your hand.
</p>
<p>
    - Set the function generator to produce an 8 V p-p, 100 Hz triangle wave.
</p>
<p>
    - Disconnect the BNC patch cord from the function generator output and connect the BNC clip leads. Connect your red LED to the clip leads (like you did
    with the photodiode in Exp. 2.3 Part B).
</p>
<p>
    - Hold the LED directly above the photodiode and observe v<sub>out</sub>.<strong> Is it less distorted than in Lab 2?</strong> Switch the function
    generator to sine wave and observe the waveshape.
</p>
<p>
    - Switch the function generator to square wave and increase the amplitude to maximum. Slowly separate the LED from the photodiode, adjusting the alignment
    to maintain the best signal (just like Lab 2). What is the maximum distance you can get with this configuration and still get a recognizable square wave
    signal? <strong>How does it compare with what you got in Lab 2?</strong>
</p>
<p>
    - Remove the BNC clip leads, reduce the amplitude of the function generator, and reconnect the BNC patch cord. Unplug the photodiode.
</p>
<p>
-    <strong>Analyze the transresistance amplifier using the op-amp design rules and show that v<sub>out</sub> does equal ?R<sub>F</sub>i<sub>d</sub>.</strong>
</p>
<h3>
    Part B: Microphone Amplifier
</h3>
<p>
The microphone we used in Lab 2 is called a <em>dynamic</em> microphone. The microphone that is housed in a telephone handset is called a    <em>carbon-button</em> (or <em>carbon</em> for short) microphone. The output of the carbon microphone is close to our standard 1 V level, but for the
    dynamic microphone to be useful, we will need to amplify its output. If we don't mind the change of sign (which we don't for this application), we have
    just the circuit we need.
</p>
<p>
    We will use this circuit in several subsequent labs, so build it in a convenient part of the breadboard (see discussion in "Organizing your Breadboard"
    above) and leave it assembled when lab is over.
</p>
<p>
    - Look back in your lab notebook to find the value you measured for the output voltage of the dynamic microphone. <strong>Calculate the gain G</strong>
    required to amplify this to a 1 V p-p signal.
</p>
<p>
    - <strong>Calculate the value of R<sub>1</sub></strong> that will give the circuit below a gain of G:
    <br/>
    <img width="314" height="177" src="../figs/img177.png"/>
</p>
<p>
    - Wire the above circuit by modifying your circuit from Part A, and connect v<sub>in</sub> to J1-6-left (Pin 8 on the Interface Board socket strip). Plug
    the dynamic microphone into J1-6.
</p>
<p>
    - Speak into the microphone and observe v<sub>out</sub>. Does it have the amplitude you expected? If not, adjust R<sub>1</sub> until v<sub>out</sub> is
    approximately 1 V p-p when speaking in a normal voice.
</p>
<h3>
    Part C: Mixer
</h3>
<p>
    We want to be able to use both the dynamic microphone and the carbon microphone. We could build separate amplifiers for each and switch back and forth, but
    it would be more convenient to be able to use either one (or both) with no changes to the circuit.
</p>
<p>
    Since Kirchhoff's Current Law must hold true at the negative input/virtual ground, if more than one current source is connected to it, the output voltage
    must be proportional to the sum of the currents. Consider the following circuit:
    <br/>
    <img width="311" height="173" src="../figs/img178.png"/>
    <br/>
    - <strong>Show in your report that the output is a weighted sum of its inputs</strong>, in other words:
    <br/>
    <img width="173" height="30" src="../figs/mixereqn.png"/>
</p>
<p>
    We can use this circuit as a <em>mixer</em> to amplify both the dynamic microphone output and the carbon microphone output by the appropriate amount, and
    then combine them into a single signal.
</p>
<p>
    - First construct the carbon microphone interface.
</p>
<DT>
<DD>
<p>
    o Note: the carbon microphone is a resistive, or passive transducer. This means that it doesn't convert acoustical energy to electrical energy directly,
    but instead the acoustical energy varies some electrical parameter (i.e., resistance). In order to interpret this change in resistance, the transducer
    needs to be powered by an external source which then produces a voltage output corresponding to the change in resistance. We do this by powering the carbon
    microphone with a voltage source in series with a large resistor (i.e., creating a voltage divider circuit).
</p></DD>
<DD><p>
    o The following circuit should do nicely. Wire this circuit to the right of your dynamic microphone amplifier, and we will connect the two in a couple of
    steps. (The carbon microphone is pins 12 and 13 on the interface connector. There is a ground on pin 14).
    <br/>
    <img width="301" height="160" src="../figs/img179.png"/>
</p></DD>
<p>
    - Plug the handset into J1-7. Speak into the handset microphone and verify that the above circuit works. Speak in the same normal voice you used for the
    dynamic microphone and <strong>measure the peak-to-peak amplitude of the signal</strong>.
</p>
<p>
    - We need to get rid of the pesky DC offset in the carbon microphone output. On the scope we can do this by switching to the AC position. Or instead, we
    can put a capacitor in series with the input. Putting it all together gives us the following circuit:
    <br/>
    <img width="537" height="192" src="../figs/img180.png"/>
</p>
<p>
    - <strong>Compute the value of R<sub>2</sub></strong> required to give an output of 1V p-p. Put together your two subcircuits and create the above circuit.
</p>
<p>
    - Speak into each microphone and verify that v<sub>out</sub> is about 1 V p-p in each case.
</p>
<p>
    - Since the op-amp can drive a 100&#8486; resistance to more than our standard voltage level, and since the handset earpiece resistance is greater than
    100&#8486;, we should be able to drive it from the op-amp output. Connect one side of the earpiece (Pin 11 on the interface board) to ground (Pin 14).
    Connect the other side (Pin 10) to v<sub>out</sub>. Have your lab partner speak into the dynamic microphone while you hold the handset to your ear and
    speak into its microphone. Verify that both voices are audible simultaneously.
</p>
<p>
    - Do not dissemble this circuit. We will use it in subsequent labs.
</p>
</DT>
