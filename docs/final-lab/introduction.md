ELEC 240 Lab

------------------------------------------------------------------------

## The Project Objective

In this final project, we will be seeing (and hearing) how our body uses
electricity to communicate. The first step to doing this is to sense the
electrical activity. Electrodes are electrical conductors that sense ion
distributions on tissue and convert that ion current into an electrical
current. For this project, we will pick a noninvasive option for sensing
bioelectrical signals by using body surface electrodes to detect the
electrical activity that occurs when a muscle contracts.

This electrical activity is in the microvolts range and not detectable
directly by our lab instruments. So we will need to amplify and filter the
signal, and create appropriate interfacing that will allow us to both
visualize and hear the signal, and give us some interesting information about
it.

## Muscle Bioelectrical Signals

When you decide to move a muscle, upper motor neurons from your motor cortex
travel to your spinal cord where they synapse with lower motor neurons. These
lower motor neurons synapse with multiple muscle fibers to form a motor unit.
Each muscle fiber is made up of actin/myosin chains that slide across each
other when there is a specific voltage potential, changing the muscle fiber
shape.

When a motor neuron fires an electrical impulse creating an action potential,
acetylcholine is released at the synapse, or the neuromuscular junction,
causing a change in the electrical potential of the muscle. This causes
voltage-gated calcium channels to open and propagate the action potential
across the muscle cells, creating a muscle contraction.

The action potentials that occur in the muscle can be sensed by body surface
electrodes. We will build an instrument called an electromyogram (EMG) that
will amplify and process this signal into a detectable and informative signal.

If you'd like to learn more about this process and how you can simulate simple
neurons, ELEC382: "Introduction to Computational Neuroscience" is a great course
for it!
