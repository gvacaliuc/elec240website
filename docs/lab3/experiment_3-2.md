ELEC 240 Lab

------------------------------------------------------------------------

Experiment 3.2
--------------

Filters and Transfer Function
-----------------------------

### 

### Equipment

* Test board
* 2.2 kΩ Resistor
* 0.33 µF [Capacitor](../misc_images/#ceramic-caps2)

### Part A: Measuring the Transfer Function

Measuring the transfer function of an RC circuit is considerably more involved
than measuring the attenuation of a resistive voltage divider.  We have to make
the measurement at a number of frequencies, and we must measure phase as well
as amplitude.

1. Select a 2.2 kΩ Resistor and a 0.33 µF [Capacitor](../misc_images/#ceramic-caps2).

    !!! note
        Ceramic capacitors use the same labeling codes as the
        potentiometers except that the units are picofarads (pF) instead of
        ohms. So a 0.33 µF capacitor would be a 330,000 pF capacitor which would
        have the code 334 = $33*10^4$.

2. Wire the following circuit:

    <center>
    ![](./figs/img171.png)
    </center>

3. Connect the `FGEN` to supply $v_{in}$ and the oscilloscope to measure $v_{out}$.

4. Using the technique described in the previous section, measure the frequency
   response of the circuit at the following frequencies: 20 Hz, 50 Hz, 100 Hz,
   200 Hz, 500 Hz, 1 kHz, 2 kHz, 5 kHz, 10 kHz, and 20 kHz.

5. **Plot the magnitude of the transfer function vs. frequency** on loglog axes
   and the phase on semilog axes. This can be done by hand or in Matlab.

6. Using Matlab, compute and plot the expected transfer function for the
   circuit you built. **How well does this compare with what you measured?**

    !!! caution
        Leave this circuit assembled. We will use it in the next experiment.
