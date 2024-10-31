from quantumtools.tensorsim import quantumcircuit, single_qubit_gate, cnot_gate

# Define state |100> and quantum circuit
state = (1, 0, 0)
qc = quantumcircuit(state)

# Applying gates

# |101> - Apply X gate on the third qubit
qc = single_qubit_gate(qc, "X", 2)
# (1/√2) * (|111> + |101>) - Apply Hadamard on the second qubit
qc = single_qubit_gate(qc, "H", 1)
# (1/√2) * (|110> + |101>) - Apply CNOT with control on the second and target on the third qubit
qc = cnot_gate(qc, 1, 2)

# Print state vector of qc
print(qc)
