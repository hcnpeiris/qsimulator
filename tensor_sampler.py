from quantumtools import histogram
from quantumtools.tensorsim import single_qubit_gate, quantumcircuit,cnot_gate, sampler

# Create a qubit system and adding gates
state = (0,0,1,0)
qc = quantumcircuit(state)
qc = single_qubit_gate((qc), 'H',1)
qc = single_qubit_gate((qc), 'X',0)
qc = single_qubit_gate((qc), 'H',0)
qc = cnot_gate(qc,0,1)

# Sampling
results = sampler(qc, 1000000)

# Plot the histogram
histogram(results)
