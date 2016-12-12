
<h3>ELEC 240 Lab<hr></h3>


<center>

<h2>
Experiment 6.2
</h2>
<h2>
The Spectrum of Acoustic Signals
</h2>
</center>
<h3>

<h3>
    Equipment
</h3>
<ul>
<li>Test board
<li>Telephone handset
<li>Mobile phone
</ul>
<h3>
    Part A: The Spectrum of Speech Signals
</h3>
<p>
    - Connect the power supply to your breadboard (if you haven't already done so), plug the dynamic microphone into J1-6, and verify that the mixer circuit you build last week still works.
</p>
<p>
    - Connect CH1 of the scope and A/D input 4 to v<sub>out</sub> of the mixer circuit.
</p>
<p>
    - Set the spectrum analyzer to dB magnitude scale and Linear frequency scale.
</p>
<p>
    - Produce a sustained vowel (a, e, i, o, u) sound. Note the form of the spectrum. It should consist of a series of peaks, like the signals from the
    function generator, but unlike the function generator signals where the harmonics fall off monotonically, the amplitudes of the harmonics in a speech
    signal rise and fall with increasing frequency.
</p>
<p>
    - To make it easier to study the spectrum, you can "freeze" the display by pressing the STOP button (continue producing the sound until the freezing is
    complete). If you like, you can get a printout of the display by selecting "Print Window" from the File menu.
</p>
<p>
    - Estimate the fundamental frequency (pitch) of the waveform. Notice that unlike the function generator signals, the fundamental is not necessarily the
    strongest component.
    <br/>
    It may be difficult to get an accurate estimate if the fundamental is low in frequency (e.g. a male voice). One way to improve accuracy is to find the
    frequency of one of the higher harmonics and divide by its order.
</p>
<p>
    - While trying to keep the same pitch, produce different sustained vowel sounds. Note how the "envelope" of the spectrum (the line connecting the tips of
    the peaks) changes while the positions of the lines remains the same.
</p>
<p>
    - Now, produce the same sustained vowel sound (your choice) while varying the pitch. Notice how the overall shape of the spectrum remains the same as the
    lines move up and down.
</p>
<p>
    - Play some music from a single musical instrument from your phone, into the microphone. Note the nature of the spectrum.
</p>
<p>
    - A soft whistle should be very close to a pure tone. Whistle a tone of about 1 kHz into the microphone and see if this is the case.
</p>
<p>
    - Plug in the telephone handset. Verify that the carbon microphone input to the mixer still works by speaking into the handset microphone.
</p>
<p>
    - Whistle the same note into the handset microphone and observe the spectrum display. Does it have the same harmonic content as with the dynamic
microphone? Since the acoustic signal was the same, the difference must be caused by distortion in the microphone.    <strong>Which microphone has the least distortion? </strong>
</p>
<p>
    - Blow into the microphone and note the shape of the spectrum. This is a <em>broadband</em>, random signal.
</p>
<p>
    - Produce an 'sh' sound. Note the shape of the spectrum. This is called an <em>unvoiced fricative</em>.
</p>
<p>
    - Now try a 'zh' sound (a <em>voiced fricative</em>). How does its spectrum compare with the one in the previous step?
</p>
<p>
    - Based on your observations of different speech sounds<strong>, can you determine an approximate bandwidth for speech?</strong> i.e. is there a frequency
    below which "most" of the energy of the speech signals is concentrated?
    <br/>
    <br/>
</p>
<h3>
    Part B: Analyzing an Unknown Signal
</h3>
<p>
    - Plug the sound card cable from the Lab PC into J2-1.
</p>
<p>
    - We want to be able to hear the signal, so connect one side of the handset earpiece to the mixer output. Ground the other side of the handset earpiece.
</p>
<p>
    - To play the sound card through our mixer, we will need to add a third input. To do this, add a 100-k&#8486; resistor (R<sub>3</sub>)to the mixer
    circuit so that it looks like this:
    <br/>
    <img width="537" height="241" src="../figs/img182.png"/>
</p>
<p>
    - Connect the sound card line out (pin 20 on the interface board socket strip) to v<sub>sound</sub>.
</p>
<p>
    - Unplug the dynamic microphone from J1-6. Unscrew the cover from the mouthpiece of the telephone handset, and remove the microphone cartridge. Now the
    only input to the mixer is from the sound card.
</p>
<p>
    - Download and play the <a name="Mystery"></a><a href=../signals/shepard30.au>Mystery Signal</a> from Lab 2 (with
    any Windows default player). You should be able to hear it through the earpiece and see it on the spectrum analyzer display.
</p>
<p>
    - It may be easier to see what's going on if you set the spectrum analyzer display to linear magnitude and log frequency.
</p>
<p>
    - Based on what you see on the spectrum display, can you explain how the mystery signal works? Hint: focus on a single peak and note how it changes from
    one tone to the next.
</p>
<p>
    - Put the telephone handset back together.
</p>
<p>
    - Exit the spectrum analyzer program. Disconnect the DAQ cable from the interface board by using the ejector levers. Do not try to remove it by pulling on
    the cable.
</p>
</DT>
