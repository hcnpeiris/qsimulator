import numpy as np
import random

# Define quantum circuit
def quantumcircuit(state):
    if isinstance(state, int):
        state = (state,)
    
    state_vectors = [np.array([1, 0]) if x == 0 else np.array([0, 1]) for x in state]
    result = state_vectors[0]
    for state_vector in state_vectors[1:]:
        result = np.kron(result, state_vector).astype(complex)
    
    return result.reshape(-1, 1)

# Define basic gates
gates = {
    "I": np.array([[1, 0], [0, 1]]),
    "X": np.array([[0, 1], [1, 0]]),
    "Y": np.array([[0, -1j], [1j, 0]]),
    "Z": np.array([[1, 0], [0, -1]]),
    "H": (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]),
    "CNOT": np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
}
I = np.array([[1, 0],
              [0, 1]]) 
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

def single_qubit_gate(quantum_circuit, gate_name, qubit_index):
    gate = gates.get(gate_name)
    if gate is None:
        raise ValueError(f"Gate '{gate_name}' not defined in gates dictionary.")
    
    num_qubits = int(np.log2(len(quantum_circuit)))
    operation = 1
    for i in range(num_qubits):
        if i == qubit_index:
            operation = np.kron(operation, gate) if isinstance(operation, np.ndarray) else gate
        else:
            operation = np.kron(operation, gates["I"]) if isinstance(operation, np.ndarray) else gates["I"]
    return operation @ quantum_circuit

def cnot_gate(quantum_circuit, control_qubit_index, target_qubit_index):
    result = cnot_operation(quantum_circuit, control_qubit_index, target_qubit_index)
    new_state_vector = result @ quantum_circuit
    return new_state_vector

def cnot_operation(quantum_circuit, control_qubit_index, target_qubit_index):
    if control_qubit_index < target_qubit_index:
        CNOT = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]])
    else:
        CNOT =  np.array([[1, 0, 0, 0],
                         [0, 0, 0, 1],
                         [0, 0, 1, 0],
                         [0, 1, 0, 0]])
    num_qubits = int(np.log2(len(quantum_circuit)))
    qubit_index =0
    operations = []
    while qubit_index <= num_qubits-1:
        if qubit_index == control_qubit_index or qubit_index == target_qubit_index:
            operations.append(CNOT)
            size = 2**((abs(target_qubit_index -control_qubit_index))-1)
            operations.append(np.eye(size))
            diff = (abs(target_qubit_index -control_qubit_index)+1)
            qubit_index = qubit_index + diff
        else:
            operations.append(I)

            qubit_index = qubit_index + 1
    result = operations[0]
    for mat in operations[1:]:
        result = np.kron(result, mat)
    return result

def states(quantum_circuit):
    num_qubits = int(np.log2(len(quantum_circuit)))
    states = []
    for i in range(2 ** num_qubits):
        state = bin(i)[2:].zfill(num_qubits)  
        states.append(state)
    return states

# Define sampler
def sampler(quantum_circuit, shots):
    allstates = states(quantum_circuit)
    probabilities = np.abs(quantum_circuit)**2
    probabilities = probabilities.flatten()
    outcomes = random.choices(allstates, probabilities, k=shots)
    return outcomes

# Define expectation value function
def expectation_value(quantum_circuit, observable, qubit_index):
    appliedvec = single_qubit_gate(quantum_circuit, observable, qubit_index)
    value = np.vdot(quantum_circuit, appliedvec)
    return value.real
