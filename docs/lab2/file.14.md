<h3>ELEC 240 Lab<hr></h3>
<center>
<h2>
Interlude
</h2>
<h2>
The Breadboard
</h2>
</center>
Most instruments have banana plugs or BNC connectors, so
we can interconnect them with patch cords.
But as we begin to build our own circuits,
we find that
many components have different kinds of connectors
and
most just have pieces of wire
coming out of them.

<p>
<p>
To connect a single component (or maybe two) to an instrument
we can use the BNC clip leads
or alligator clips on the banana plug patch cords,
But for anything more complex, we need a
scheme
designed for connecting things with pieces of wire.
The system we will use goes by a number of names:
solderless breadboard, AP strip (after the original manufacturer), or
proto-board.
We will simply call them &quot;breadboards".
<p>
Our breadboards actually consist of two parts:
the lower portion which is the breadboard proper,
and the upper part which contains the
<i>interface modules</i>.
<p>
These are discussed in detail 
<a name=here href=/references/breadboard>here</a>.
<p>
In either case, we make connections between one
component and another by pushing the ends of pieces of wire
(possibly attached to a component) into the holes in the breadboard.
Although this is simple in concept, there is a bit of art
required to do it properly.
See 
<a name=here href=/references/wiring>here</a>
for information on the art of wiring.

<h3>The Interface Modules</h3>
<p>
The purpose of the Interface Modules is to bring signals from
other parts of the Lab Station to the breadboard for convenient
wiring.
To do this we must connect those components to the Interface
Modules via the appropriate cables.
Here is a drawing of the interface module with the names of the various
connectors.
<center>
<IMG
 WIDTH="449" HEIGHT="194" ALIGN="BOTTOM" BORDER="0"
 SRC="../figs/img158.png"
 ALT="\includegraphics[scale=0.500000]{interface.ps}">

<p>
</center>
There is a table of connector pin assignments 
<a name=here href=/references/interface>here</a>.
<p>
In the next experiment we will use the interface module to access the oscilloscope, the function generator, and the Lab PC sound card. To connect the sound card, plug the round cable from the Lab PC (with the 8-pin round connector)

<p>
<center>
<img src=../figs/din8.jpg>
</center>

<p>
<p>
into J2-1 on the interface module. To connect the oscilloscope, use a BNC patch cord to connect <tt>CH&nbsp;1</tt> of the scope to J1-1 of the Interface module. Similarly, connect <tt>CH&nbsp;2</tt> to J1-2.
