# Statevector Simulation of Quantum Circuits

This repository contains a submission for the QOSF Mentorship Program, Cohort 10, Screening Test Task 1: **Statevector Simulation of Quantum Circuits.**

This simulator simulates a quantum circuit using the Hadamard gate, X gate, and CNOT gate through two methods: 

1. Naive simulation using matrix multiplication 
2. Advanced simulation using tensor multiplication

***quantumtools*** is a custom Python package designed for simulation, including functions to generate quantum circuits, perform sampling, generate histograms, and apply gates (X, H, and CNOT) for each method.

## Table of Contents

- [Installing Dependencies](#installing-dependencies)
- [01 - Naive simulation using matrix multiplication](#01---naive-simulation-using-matrix-multiplication)
- [02 - Advanced simulation using tensor multiplication](#02---advanced-simulation-using-tensor-multiplication)
- [03 - Bonus questions](#03---Bonus-questions)
## Installing Dependencies
```bash
pip install -r requirements.txt
```
## 01 - Naive simulation using matrix multiplication
This simulator uses functions from the `matrixsim` module.

`quantumcircuit(state)` function takes an integer or tuple state as input, where each element represents a qubit (0 or 1) and generate relevant matrix

`single_qubit_gate(quantum_circuit, gate_name, qubit_index)`: Applies a specified gate (`"I"`, `"X"`, `"Y"`, `"Z"`, or `"H"`) to a specific qubit in `quantum_circuit`.

`cnot_operation(quantum_circuit, control_qubit_index, target_qubit_index)`: Applies a CNOT gate between control and target qubits in quantum_circuit.

Here is simple `quantum_circuit`
```bash
python3 matrixsimulator.py
```
### Simulator runtime vs Number of qubits
This `matrix_max_qubit` script determines the maximum number of qubits that can be simulated and plots the runtime of the simulation against the number of qubits. It randomly selects qubits to serve as the target and control qubit indices and applies the X, H, and CNOT gates to these qubits.

```bash
python3 matrix_max_qubit.py
```
*If the script was terminated before the graph was plotted, adjust the **maximum number of qubits** to the **last system qubit count** *

![Figure 1](https://github.com/hcnpeiris/statevec-sim/blob/main/images/Figure_1.png?raw=true)

## 02 - Advanced simulation using tensor multiplication
This simulator uses the `tensorsim` module. Function usage is similar to `matrixsim` but returns values using tensor multiplication.

```bash
python3 tensorsimulator.py
```
### Simulator runtime vs Number of qubits
```bash
python3 tensor_max_qubit.py
```
*If the script was terminated before the graph was plotted, adjust the **maximum number of qubits** to the **last system qubit count** *

![Figure 1](https://github.com/hcnpeiris/statevec-sim/blob/main/images/Figure_2.png?raw=true)

## 03 - Bonus questions
### 03.1 Sampler
The `sampler` function calculates the probability of each state in a quantum system and uses these probabilities to randomly select outcomes for a given number of shots. The `histogram` function generates a probability distribution of these quantum states.

```bash
python3 matrix_sampler.py
```
![Figure 1](https://github.com/hcnpeiris/statevec-sim/blob/main/images/Figure_3.png?raw=true)
```bash
python3 tensor_sampler.py
```
![Figure 1](https://github.com/hcnpeiris/statevec-sim/blob/main/images/Figure_4.png?raw=true)

### 03.2 Expectation Values

The `expectation_value` function computes the expectation value of a quantum operation applied to a state vector.  First, it calculates using matrix multiplication or tensor dot to calculate |OP|ψ⟩, and then uses the inner product to calculate ⟨ψ|Op|ψ⟩.

```bash
python3 matrix_expectation.py
```
```bash
python3 tensor_expectation.py
```
