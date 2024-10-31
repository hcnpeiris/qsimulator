from quantumtools.matrixsim import quantumcircuit, expectation_value, single_qubit_gate

state = (0,0)
qc = quantumcircuit(state)
#(1/√2) * (|00> + |11>)
qc = single_qubit_gate(qc,"H",1)

expectation = expectation_value(qc,"X",1)
print(expectation) 

