ELEC 240 Lab

------------------------------------------------------------------------

Experiment 2.1
--------------

Electroacoustic Transducers I
-----------------------------

In this section we will discover different ways to detect and change a
signal.

### Equipment

* [BNC Male to Clips test lead](../misc_images/#bnc-cliplead)
* [Oscilloscope probe](../misc_images/#vb-probe)

### Part A: Listening to a Signal

1. Set up the function generator to produce a 1-kHz sine wave with a
   peak-to-peak (p-p) amplitude of 5 Volts. Verify settings by viewing on the
   oscilloscope.

2. Using the BNC-to-clip test lead, connect the output of the function
   generator to the speaker leads. **What do you hear?**

3. With the speaker still connected to the FGEN, measure the amplitude of the
   voltage across the speaker. This time, connect an oscilloscope probe to one
   of the speaker leads. (The ground lead can remain disconnected because it is
   already internally connected to the FGEN ground). **What is the peak-to-peak
   measurement now? Why did it change?**

4. Using FGEN controls, vary the amplitude, frequency, and shape of the signal.
   **How does the nature of the sound change as these signal parameters
   change?**

5. Disconnect the speaker.

### Part B: Thevenin Equivalent and Maximum Power Transfer

Looking back at the diagram in the Background section we can see what caused
the reduction in signal amplitude (attenuation): $R_{out}$ of the function
generator and $R_L$ of the speaker form a voltage divider. To reduce the
attenuation, one possibility is to either reduce $R_{out}$ or increase $R_L$. For
this, the first step would be to determine what $R_{out}$ is.

1. Assuming that the oscilloscope provides infinite load, **determine the
   Thevenin voltage** (use same FGEN settings as in Part A).

2. Referring to the Background section, **calculate the Thevenin resistance**
   for various $R_L$: 20, 30, 50, 100 Ohms. **Does the Thevenin resistance
   vary?**

3. **Calculate the average power** dissipated by each load.

    * The amount of average power dissipated by the load is another way of stating
    the amount of average power delivered to the load.

    * $P_{avg} = 0.5*(V_m^2 * R_L)$ where $V_m$ is the maximum amplitude of voltage
    across $R_L$.  


    !!! note
        Maximum Power Transfer: The maximum power transfer theorem states that the
        maximum power is delivered to the load when the load resistance is equal to the
        Thevenin resistance of the source. This is important in applications such as
        when the load is a cell phone antenna and you need maximum power delivered to
        improve coverage area; another example is the load being an audio speaker that
        requires maximum power to deliver the highest sound level.

4. **Make a graph of $P_{avg}$ vs. $R_L$** and show how the maximum power
   transfer theorem is verified by these results.
