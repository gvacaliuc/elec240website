<h3>ELEC 240 Lab<hr></h3>
<center>
<h1>
The Breadboard
</h1>
<h1>
 
</h1>
</center>

<h3>The Concept</h3>
<p>
When building a &quot;permanent circuit" the components can be
&quot;grown" together (as in an integrated circuit),
soldered together (as on a printed circuit board),
or held together by screws and clamps (as in house wiring).
In lab, we want something that is easy to assemble and easy to change.
We also want something that can be used with the same components that
&quot;real" circuits use.
Most of these components have pieces of wire or metal tabs sticking
out of them to form their terminals.
<h3>How it Works</h3>
<p>
The heart of the solderless breadboard is a small metal clip
that looks like this:
<center>
<img src=../figs/ap4.jpg>
</center>
Each of the pairs of fingers is mechanically independent from the others, so
we can insert the end of a wire between any pair
without reducing the tension in any of the other fingers. However when we insert a wire between any pair, we electrically connect all metal fingers together.
<p>
To make a breadboard, an array of these clips is embedded in
a plastic block which holds them in place and insulates
them from each other, like this:
<center>
<img src=../figs/ap2.jpg>
</center>

<p>
Depending on the size and arrangement of the clips, we get
either a socket strip or a bus strip.

The socket strip is used for connecting components together.
It has two rows of short (5 contact) clips
arranged one above another, like this:
<center>
<IMG
 WIDTH="561" HEIGHT="102" ALIGN="BOTTOM" BORDER="0"
 SRC="img1.gif"
 ALT="\includegraphics[scale=0.650000]{socket.ps}">


</center>

The bus strip is used to distribute power and ground voltages
through the circuit.
It has has six long (24 contact) clips
arranged lengthwise, like this:
<center>
<IMG
 WIDTH="534" HEIGHT="24" ALIGN="BOTTOM" BORDER="0"
 SRC="img2.gif"
 ALT="\includegraphics[scale=0.650000]{bus.ps}">


</center>
Note that the bus strip is not electrically connected in the center. If you want a single, continuous bus, you will have to bridge that central gap yourself.
<p>
When we combine two socket strips, three bus strips,
power connectors, power tie points, interface modules,
and an interface connector on a large printed circuit board,
we get the complete breadboard:
<center>
<IMG
 WIDTH="634" HEIGHT="489" ALIGN="BOTTOM" BORDER="0"
 SRC="img3.gif"
 ALT="\includegraphics[scale=0.750000]{sb_123.ps}">


</center>
(In this picture we have replaced the plastic covers, hiding the
connection between the terminal points).
<p>
The breadboard lets us connect components together
and by wiring the bus strips to the binding posts and the binding
posts to the power supply, to connect the power supply to the
circuit.
Now what we need is a way to bring
connections from the rest of the instruments into the breadboard.
