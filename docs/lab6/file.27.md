ELEC 240 Lab

------------------------------------------------------------------------

Prelude: Decibels
-----------------

You've probably heard the term \*decibel\* used in conjunction with
sound levels: having a muffler louder than 85 dB will get you a ticket,
listening to music at 110 dB will damage your hearing. You've probably
also noticed the button marked \`\`\`ATT -20dB\`\`\` on the function
generator, so decibels don't just have to do with sound. So what exactly
is a decibel? It's a logarithmic way of expressing the ratio of two
power levels (or sound pressure levels, or voltage levels, or any other
kinds of levels). More precisely, \${\\rm power\\: ratio\\: in\\: dB} =
10 \\log\\left(\\frac{P\_1}{P\_0}\\right)\$ where \$P\_0\$ and \$P\_1\$
are the two powers being compared, and \$\\log()\$ is the common, or
base 10 logarithm. If we have two \*voltage\* levels, \$V\_1\$ and
\$V\_2\$ across the same load resistance, \$R\_L\$, then \$10
\\log\\left(\\frac{P\_1}{P\_0}\\right) = 10
\\log\\left(\\frac{{V\_1}\^2/R\_L}{{V\_2}\^2/R\_L}\\right) = 20
\\log\\left(\\frac{V\_1}{V\_0}\\right).\$ Why logarithmic? The smallest
perceivable sound level corresponds to an acoustic power density of
approximately \$10\^{-12}\~\\text{W}/\\text{m}\^2\$. But the level at
which the sensation of sound begins to give way to the sensation of pain
is about \$1\~\\text{W}/\\text{m}\^2\$. To cope with this large dynamic
range without loosing track of the number of zeros after the decimal
point, a logarithmic scale is useful. It's important to remember that a
decibel measurement expresses a \*ratio\*. So it always makes sense to
say that a signal \$x\$'s amplitude is so many dB greater (or less) than
signal \$y\$'s amplitude. But if we say that a signal is \*equal\* to
some number of decibels, then there must be a reference level. For
sound, that reference level is usually taken as
\$10\^{-12}\~\\text{W}/\\text{m}\^2\$ which corresponds to a pressure of
\$10\^{-5}\\text{N}/\\text{m}\^2\$. If we call this the reference
pressure level, \$p\_0\$, we get the definition of \*sound pressure
level\* \${\\textrm SPL} = 20 \\log\\left(\\frac{p}{p\_0}\\right)\$
(where we use 20 instead of 10 since power is proportional to the square
of the pressure). In a circuit, the choice of a reference level is not
quite so obvious. For voltages, the typical choice is 1 V, which gives
"decibels relative to 1 Volt" or dBV for short. Other forms you may
encounter are dBW (relative to 1 watt) or dBm (relative to 1 mW). It is
sometimes stated that the response of a filter falls off at "20dB per
decade" or "6dB per octave". This is just another way of saying that the
response varies as 1/f. In other words, if \$f\_2\$ is 10 times \$f\_1\$
(i.e. the frequencies are separated by one decade) then \$\\vert
H(f\_2)\\vert\$ will be 1/10 of \$\\vert H(f\_2)\\vert\$. Since \$20
\\log(1/10) = -20\$ then we have a loss of 20 dB (or a gain of -20 dB)
for each decade increase in frequency. Similarly, for two frequencies
separated by one octave (a factor of two) we would have \$20 \\log(1/2)
= -6.02\$ or approximately 6 dB per octave. For more information, check
out the article on
[Decibels](http://artsites.ucsc.edu/ems/music/tech_background/te-06/teces_06.html)
at UCSC Electronic Music Studios.
