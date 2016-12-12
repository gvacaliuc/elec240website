
<h3>ELEC 240 Lab<hr></h3>


<center>
<h2>
Experiment 2.2
</h2>
<h2>
Electroacoustic Transducers II
</h2>
</center>
<p>
    In this section we will discover different ways to detect and change a signal.
</p>
<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>Speaker
<li>Microphone
</ul>
<h3>
    Part A: Microphone
</h3>
<p>
    So far we have used an acoustic output device, the speaker, to convert electrical signals to sound. Now we need an input device to convert acoustic signals to electric ones.
</p>
<p>
    - Get a microphone from the supply room. It has two connectors: we will use the larger one.
    <br/>
    <img width="320" height="240" src="../figs/mic_conns.jpg"/>
</p>
<p>
- Use a BNC patch cord to connect CH1 of the oscilloscope to J1-1 of the test board (refer to the    <a href=/references/interface>test board pin assigments</a>).
</p>
<p>
    - Plug the microphone into J1-4 of the test board.
</p>
<p>
    - Take a piece of wire and strip 6-7 mm of insulation from each end. The end of the wire should look like this:
    <br/>
    <img border="0" width="275" height="158" src="../figs/stripped.jpg"/>
</p>
<p>
<DT>
<DD>    o**Note: The stripped length of a wire is very important. If it is too short, the insulation can prevent contact within the socket resulting in an intermittent connection. THIS IS ONE OF THE MOST COMMON PROBLEMS IN THE LAB. If it is too long, the exposed portion of the wire can short to other wires.**
</p></DD>
<p>
    - Plug one end of the wire to <a href=/references/interface>pin1</a> and the
    other end to <a href=/references/interface>pin 4</a>. This will connect the
    microphone to the scope (CH1). The grounds are automatically connected by the test board.
    <br/>
    <em>
        <img border="0" width="427" height="320" src="../figs/photo2.2.1a1.jpg"/>
    </em>
</p>
<p>
    - Ensure the following settings on the oscilloscope:
</p>

<DD><p>
    o CH1
</p></DD>
<DD><p>
    o Volts/Div : 5mV
</p></DD>
<DD><p>
    o Time/Div: 1ms
</p></DD>
<DD><p>
    o 1X setting on CH1
</p></DD>
<p>
    - Speak, sing, or whistle into the microphone and observe the signal on the scope. If the amplitude is too small, you can use the Volts/Div setting to get
    a little more resolution.
</p>
<p>
    - Experiment with the Time/Div settings to see what effect it has on the display.
</p>
<p>
- Trigger: Drag the trigger icon (arrow followed by a T) just outside the signal display so that it crosses the signal.    <strong>What happens to the display?</strong>
</p>
<DD><p>
    o What is Trigger? The oscilloscope has to continually refresh its display since a continuous signal is being fed to it. If each MISSINGDATAsweepMISSINGDATA (refresh of data)
    started at a different place on the signal all we would get is a jumble of waveforms. The trigger sets an origin from which each sweep should start. That
    way, particularly for periodic signals, the new waveform traces onto the old waveform and the signal appears static.
</p></DD>
<p>
    - Measure the amplitude of the signal.
</p>
<p>
    - Produce a sustained vowel sound. <strong>Which appears most sinusoidal?</strong>
</p>
<p>
    - Continue producing a sustained vowel sound and measure its frequency (by measuring the period).
</p>
<p>
    - If you are musically inclined, sing or whistle the note <em>A</em> and measure its frequency. Otherwise search for the tone and play it on your phone. How does
    your measured frequency compare with the <em>official</em> value for the frequency of <em>A</em>?<strong>If there is a discrepancy, explain why it might be.</strong>
</p>
<h3>
    Part B: The Lab PC as a Signal Source
</h3>
<p>
    The microphone is a device that converts an acoustic pressure into a voltage. The Lab PC contains a device, the Sound Card, that converts a sequence of
    numbers into a voltage. This sequence of numbers could represent the <em>samples</em> of a physical signal that you learned about in ELEC 241.
</p>
<p>
    Since the computer can compute functions and the sound card can produce electrical output we could use the Lab PC as our 'function generator', which can produce more interesting functions than our VirtualBench <tt>FGEN</tt> can. Another advantage is that R<sub>out</sub> of the sound card is less than that of the function generator, so we can connect the speaker directly with less signal loss. Let's look at a few examples.

</p>
<p>
    - Plug the sound card cable from the Lab PC (with the <a href=/misc_images/#din8>8-pin round connector</a>) into J2-1 on the
    test board.
</p>
<p>
    - Connect a BNC clip lead to J1-3 and the clips to the loudspeaker.
</p>
<p>
    - Connect the speaker to the sound card speaker output but connecting a piece of wire between pins 3 and 20 on the test board.
</p>
<p>
    - View the speaker output on CH1 (connect a wire from pin 20 to pin 1).
</p>
<p>
    - Listen to and observe the waveform for the following signals:
</p>
<DD><p>
    o <a href=../signals/sine.au>Signal 1</a>
</p></DD>
<DD><p>
    o <a href=../signals/gong.au>Signal 2</a>
</p></DD>
<DD><p>
    o <a href=../signals/shepard30.au>Mystery Signal</a>
</p></DD>

<p>
    - We'll look at this signal again in a few weeks when we have some more sophisticated analysis tools. In the meantime, based on what you can hear and what you can see on the scope, <strong>can you figure out the trick?</strong>
<p>
    - Disconnect speaker and sound card cable.
</p>
