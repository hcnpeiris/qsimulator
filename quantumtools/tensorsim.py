import numpy as np
import random

# Define quantum circuit
def quantumcircuit(state):
    if isinstance(state, int):
        state = (state,)
    
    tensors = [np.array([1, 0]) if x == 0 else np.array([0, 1]) for x in state]
    result = tensors[0]
    for tensor in tensors[1:]:
        result = np.kron(result, tensor)
    
    return result.reshape([2]*len(state))

# Define basic gates in a dictionary
gates = {
    "I": np.array([[1, 0], [0, 1]]),  
    "X": np.array([[0, 1], [1, 0]]),  
    "Y": np.array([[0, -1j], [1j, 0]]),  
    "Z": np.array([[1, 0], [0, -1]]),  
    "H": (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]]),  
}
I = np.array([[1, 0],
              [0, 1]]) 
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# Define gates
def single_qubit_gate(quantum_circuit, gate, qubit_index):
    gate = gates[gate] 
    state_tensor = np.tensordot(gate, quantum_circuit, axes=([1], [qubit_index]))
    state_tensor = np.moveaxis(state_tensor, 0, qubit_index)
    return state_tensor

def cnot_gate(quantum_circuit, control_qubit_index, target_qubit_index):
    CNOT_tensor = CNOT.reshape(2, 2, 2, 2)
    state_tensor = np.tensordot(CNOT_tensor, quantum_circuit, axes=([0, 1], [control_qubit_index, target_qubit_index]))
    state_tensor = np.moveaxis(state_tensor, [0, 1], [control_qubit_index, target_qubit_index])
    return state_tensor

def states(quantum_circuit):
    flat_vector = np.ravel(quantum_circuit)
    num_qubits = int(np.log2(len(flat_vector)))
    states = []
    for i in range(2 ** num_qubits):
        state = bin(i)[2:].zfill(num_qubits)  
        states.append(state)
    return states

def sampler(quantum_circuit, shots):
    all_states = states(quantum_circuit)
    flat_vector = np.ravel(quantum_circuit)
    probabilities = np.abs(flat_vector)**2
    probabilities = probabilities.flatten()
    outcomes = random.choices(all_states, probabilities, k=shots)
    return outcomes

def expectation_value(quantum_circuit, observable, qubit_index):
    appliedvec = single_qubit_gate(quantum_circuit, observable, qubit_index)
    value = np.vdot(quantum_circuit, appliedvec)
    return value.real

