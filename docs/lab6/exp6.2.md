ELEC 240 Lab

------------------------------------------------------------------------

Experiment 6.2
--------------

The Spectrum of Acoustic Signals
--------------------------------

### 

### Equipment

-   Test board
-   Telephone handset
-   Mobile phone

### Part A: The Spectrum of Speech Signals

- Connect the power supply to your breadboard (if you haven't already
done so), plug the dynamic microphone into J1-6, and verify that the
mixer circuit you build last week still works.

- Connect CH1 of the scope and A/D input 4 to v~out~ of the mixer
circuit.

- Set the spectrum analyzer to dB magnitude scale and Linear frequency
scale.

- Produce a sustained vowel (a, e, i, o, u) sound. Note the form of the
spectrum. It should consist of a series of peaks, like the signals from
the function generator, but unlike the function generator signals where
the harmonics fall off monotonically, the amplitudes of the harmonics in
a speech signal rise and fall with increasing frequency.

- To make it easier to study the spectrum, you can "freeze" the display
by pressing the STOP button (continue producing the sound until the
freezing is complete). If you like, you can get a printout of the
display by selecting "Print Window" from the File menu.

- Estimate the fundamental frequency (pitch) of the waveform. Notice
that unlike the function generator signals, the fundamental is not
necessarily the strongest component.\
It may be difficult to get an accurate estimate if the fundamental is
low in frequency (e.g. a male voice). One way to improve accuracy is to
find the frequency of one of the higher harmonics and divide by its
order.

- While trying to keep the same pitch, produce different sustained vowel
sounds. Note how the "envelope" of the spectrum (the line connecting the
tips of the peaks) changes while the positions of the lines remains the
same.

- Now, produce the same sustained vowel sound (your choice) while
varying the pitch. Notice how the overall shape of the spectrum remains
the same as the lines move up and down.

- Play some music from a single musical instrument from your phone, into
the microphone. Note the nature of the spectrum.

- A soft whistle should be very close to a pure tone. Whistle a tone of
about 1 kHz into the microphone and see if this is the case.

- Plug in the telephone handset. Verify that the carbon microphone input
to the mixer still works by speaking into the handset microphone.

- Whistle the same note into the handset microphone and observe the
spectrum display. Does it have the same harmonic content as with the
dynamic microphone? Since the acoustic signal was the same, the
difference must be caused by distortion in the microphone. **Which
microphone has the least distortion?**

- Blow into the microphone and note the shape of the spectrum. This is a
*broadband*, random signal.

- Produce an 'sh' sound. Note the shape of the spectrum. This is called
an *unvoiced fricative*.

- Now try a 'zh' sound (a *voiced fricative*). How does its spectrum
compare with the one in the previous step?

- Based on your observations of different speech sounds**, can you
determine an approximate bandwidth for speech?** i.e. is there a
frequency below which "most" of the energy of the speech signals is
concentrated?\
\

### Part B: Analyzing an Unknown Signal

- Plug the sound card cable from the Lab PC into J2-1.

- We want to be able to hear the signal, so connect one side of the
handset earpiece to the mixer output. Ground the other side of the
handset earpiece.

- To play the sound card through our mixer, we will need to add a third
input. To do this, add a 100-kΩ resistor (R~3~)to the mixer circuit so
that it looks like this:\
![](../figs/img182.png){width="537" height="241"}

- Connect the sound card line out (pin 20 on the interface board socket
strip) to v~sound~.

- Unplug the dynamic microphone from J1-6. Unscrew the cover from the
mouthpiece of the telephone handset, and remove the microphone
cartridge. Now the only input to the mixer is from the sound card.

- Download and play the []()[Mystery Signal](../signals/shepard30.au)
from Lab 2 (with any Windows default player). You should be able to hear
it through the earpiece and see it on the spectrum analyzer display.

- It may be easier to see what's going on if you set the spectrum
analyzer display to linear magnitude and log frequency.

- Based on what you see on the spectrum display, can you explain how the
mystery signal works? Hint: focus on a single peak and note how it
changes from one tone to the next.

- Put the telephone handset back together.

- Exit the spectrum analyzer program. Disconnect the DAQ cable from the
interface board by using the ejector levers. Do not try to remove it by
pulling on the cable.
