<h3>ELEC 240 Lab<hr></h3>
<center>
<h2>
Interlude
</h2>
<h2>
Grounds and Grounding
</h2>
</center>
Since a voltage is actually a
<em>difference</em>
in potential, it is always measured
<em>between</em>
two points in the circuit.
In most circuits there is a single point
(actually many physical points tied together by low
resistance conductors into a single electrical point)
with respect to which all other voltages are expressed.
This point is called the &quot;common", &quot;reference", or &quot;ground" node.
The term &quot;ground" arises from the fact that in the early days of
telegraphy, one leg of the circuit was formed by the earth itself
by driving a conductive rod into the ground at each of the two
stations
so that only a single wire was required between them.
<p>
In our circuits, we will actually use a wire, rather than dirt,
to form the ground connection,
but we must bear in mind that all of our ground
terminals
are connected together
(sometimes without our doing so explicitly).
This concept of a common ground terminal becomes important
when we look at our next two instruments,
the Function Generator and the Oscilloscope.
<p>
So far most of the the instruments and components we've used have had
their terminals connected to banana jacks.
For example, the power supply
<img src=../figs/ps_jacks.jpg>
the DMM
<img src=../figs/dvm_jacks2.jpg>
and the lamp breadboard
<img src=../figs/lamp_jacks.jpg>
<p>
The function generator and 'scope don't have banana jacks.
Instead they have what are called &quot;BNC" connectors.
These are a type of
<em>coaxial</em>
connector where the outer (ground) conductor
surrounds the inner (signal) conductor.
So instead of
<IMG
 WIDTH="133" HEIGHT="51" ALIGN="BOTTOM" BORDER="0"
 SRC="../figs/img155.png"
 ALT="\includegraphics[scale=0.400000]{fig2.ps}">


we have
<IMG
 WIDTH="133" HEIGHT="47" ALIGN="BOTTOM" BORDER="0"
 SRC="../figs/img156.png"
 ALT="\includegraphics[scale=0.400000]{fig3.ps}">



<p>
This type of connection has a number of advantages.
The shielding by the outer conductor reduces interference
<em>to</em>
low level signals and
<em>by</em>
high level ones.
The single connector allows both terminals to be connected
simultaneously.
<p>
The (sometime) disadvantage is that the outer (shield or ground)
conductors of
<em>all</em>
the BNC connectors on
<em>all</em>
our instruments are connected together.
Within one instrument they are connected together by the metal chassis.
Since the chassis is connected to the third (ground) terminal of
the power cord, the chassis (and hence the grounds) of all
the instruments are connected together.
Later we'll see how this can be a disadvantage.
For now, let's avail ourselves of some of the advantages.
