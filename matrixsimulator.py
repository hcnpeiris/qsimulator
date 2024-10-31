from quantumtools.matrixsim import quantumcircuit, single_qubit_gate, cnot_gate

# Define state |000> and quantum circuit
state = (0, 0, 0)
qc = quantumcircuit(state)

# Applying gates

# |100> - Apply X gate on the first qubit
qc = single_qubit_gate(qc, "X", 0)
# (1/√2) * (|100> + |110>) - Apply Hadamard on the second qubit
qc = single_qubit_gate(qc, "H", 1)
# (1/√2) * (|100> + |111>) - Apply CNOT with control on the second and target on the third qubit
qc = cnot_gate(qc, 1, 2)

# Print state vector of qc
print(qc)
