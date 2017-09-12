ELEC 240 Lab

------------------------------------------------------------------------

Experiment 3.1
--------------

Resistive Voltage Dividers
--------------------------

### Equipment

-   Test board
-   Resistors
-   1-kΩ Potentiometer

[BNC T Connector](/misc_images/#bnc-t)

### Part A: Measuring AC Voltage with the DMM

- Connect the BNC T-connector to CH1 of the scope.

- Use a BNC patch cord to connect one end of the T to the `FGEN` output.
Connect a BNC clip lead to the other end of the T.\
![](../figs/img200.png){width="350" height="288"}

- Set the `FGEN` to produce a 2-V peak-to-peak, 100Hz sine wave.

- Set the DMM to AC Volts and connect the probes to the clip leads.
**What is the voltage reading on the DMM?**

- Set the `FGEN` to produce a square wave. What is the voltage reading
on the DMM?

- Reset the `FGEN` to sine wave. Note the reading on the DMM at 5 Hz, 50
Hz, 500 Hz, 5 kHz, and 50 kHz.

- **What is the useful frequency range of the DMM for measuring AC
signals?**

o The AC voltage function of the DMM is calibrated to read
(approximately) the *RMS* value of the waveform. RMS stands for
root-mean-square i.e. the square root of the mean value of the square of
the function:\
**![](../figs/rmseqn.png){width="185" height="62"}**

o We'll see the importance of this when we study power. For now just
remember that for a sine wave, V~RMS~ = 0.707 V~peak~. ****

### Part B: The Basic Voltage Divider

- Wire the following circuit using 10kΩ (brown-black-orange) resistors
for both R~1~ and R~2~:\
**![](../figs/img162.png){width="348" height="151"}**

- **What should the voltage divider ratio (v~out~/v~s~) be?**

- Set the `FGEN` to produce a 2 V p-p sine wave.****

- **Measure v~out~ with the oscilloscope. Is it what you expect?**

- Change R~1~ and R~2~ to 47Ω (yellow-violet-black). **What is the
output voltage?**

- Now change R~1~ and R~2~ to 1MΩ. **What is the output voltage?**

o No circuit exists in isolation. To be useful its input or output (or
both) should be connected to some other circuit. Unfortunately the
interaction between the circuit and a non-ideal source or load causes it
to behave differently than it would in an idealized situation. With
careful design, this interaction can be minimized or accounted for. If
ignored it can reduce the performance of the system, or keep it from
working altogether.****

- A more accurate model of the system we measured would be:\
**![](../figs/img163.png){width="369" height="95"}**

- Based on your measurements, **what are the output resistance (R~S~) of
the function generator and the input resistance (R~L~) of the scope?**

### Part C: The Potentiometer

- A potentiometer (pot for short) is a fixed value resistor with a
third, movable contact or *slider* which may be positioned anywhere
along the resistive element. If we represent the position of the slider
by α, where α varies between 0 (fully counterclockwise) and 1 (fully
clockwise), then the resistance between the lower end of the resistor
and the slider will be αR and between the slider and the upper end will
be (1-α)R, where R is the total resistance of the potentiometer.

- If we connect the two fixed contacts to a voltage source and measure
the output between the movable contact and one fixed contact, we get a
variable voltage divider:\
![](../figs/img164.png){width="521" height="143"}

- Then the output is:\
![](../figs/poteqn.png){width="352" height="48"}

- Select a 10kΩ. It will have three short wires sticking out in a
triangular pattern. The center terminal is the slider contact and the
two outer terminals are the fixed contacts.\
![](../figs/pots.jpg){width="377" height="196"}

o *Note: Figuring out the value of a pot can be tricky. Some pots are
labeled directly with the value (e.g. "100" or "10K"). Others are
labeled using the same code as for fixed resistors, except that numbers,
rather than colors, are used. For example, a 10kΩ resistor would have
the bands brown-black-orange. The values of these colors are 1, 0, and
3, so a 10kΩ pot would have the label "103".*

- Wire the following circuit:\
![](../figs/img165.png){width="366" height="121"}

- Set the function generator to produce a 2 V p-p 100-Hz sine wave.

- Set the potentiometer adjustment screw to midscale and **measure
v~out~.**

- The pot has a scale divided into 10 equal divisions, presumably
representing 10 equal divisions of resistance. Set the pot to each of
these 10 divisions and measure v~out~. **Is this presumption correct?**

### Part D: Thevenin Equivalent Circuit of a Microphone

- Recall that the Thevenin theory states that any DC circuit can be
modeled as a power source and resistance. If a known resistive load is
attached to a 'blackbox' circuit, such as an unknown power supply, the
Thevenin equivalence can be found for this blackbox circuit. **How do
you find the Thevenin equivalent circuit?**

- Another advantage of knowing the Thevenin equivalence of a blackbox
circuit is that we can determine a load resistance that maximizes the
power transfer to the load. **What should the load resistance be for
maximum power transfer?**

o Note: Thevenin theory not only applies to power supplies and function
generators, but also to sensors. When sensors detect signals and provide
some outputs, they can be considered as sources with dependent voltage
or current supplies.

o Recall that a speaker produces sound by converting current flowing
through the voice coil into mechanical motion of the speaker cone. By
reversing this process, it is also possible to use a speaker as a
microphone. Sound waves will cause the speaker cone and voice coil to
move. As the voice coil moves through the permanent magnet, a current is
induced in the voice coil and a voltage appears across the voice coil.

- Two speakers will be used here as a pair. One of them is the speaker,
converting the sine wave generated from function generator to sound. The
other plays the role of a microphone, and reverses the sound to
electrical waves. They are connected as below.\
![](../figs/img201.png){width="273" height="273"}

- Now the two wires connected to the microphone (the upper speaker) can
be considered as the two terminals of the load resistance. The whole
system consisting of the function generator, the speaker and the
microphone should be seen as a circuit with a sine wave power supply
(Thevenin voltage) and an internal resistance (Thevenin resistance).

- Set the `FGEN` to generate a sinusoid within audible range and connect
the upper speaker (microphone) to the oscilloscope. **Measure the
peak-to-peak amplitude, which will be the Thevenin voltage.**

- Connect different resistances between 1 and 10 ohms to the output of
the microphone and measure the load voltage V~L~ of these resistances.

- **Calculate the Thevenin resistance of the system for each load and
the power transferred to each load resistance. What is the average
Thevenin resistance and is there any significant variation between
measurements?**

- **Draw the power vs. resistance diagram** and find the maximum point.

****
