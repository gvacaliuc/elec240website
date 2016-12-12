<h3>ELEC 240 Lab<hr></h3>
<center>
<h2>
Interlude
</h2>
<h2>
Standard Signal Levels
</h2>
</center>
<p>
In the next experiment, we are going to build an amplifier to
increase the &quot;low" output voltage of the microphone
to a &quot;usable level."
What should that level be?
<p>
There are several criteria we could use.
In the previous experiments we found that there was a maximum
output
signal level the op-amp can produce without clipping.
Clearly our standard level should be less than this.
In fact it should be significantly less to allow for
peaks which exceed the &quot;average" value of the signal.
(Recording engineers call this &quot;headroom.")

Another criterion would be to have a standard signal level which
is compatible with our signal sinks.
A signal of about 0.5 to 1.0&nbsp;V p-p gives a fairly loud sound
when connected to the handset earpiece, the speaker, or the sound
card line in.
Since 1&nbsp;V is a nice round number, and is comfortably less
than the clipping level, we will choose 1&nbsp;V p-p as our standard
signal level.
