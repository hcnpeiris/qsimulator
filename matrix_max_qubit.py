from quantumtools.matrixsim import single_qubit_gate, cnot_gate, quantumcircuit
import random, time
import matplotlib.pyplot as plt

n_qubits = []
runtimes = []

""" Plots the runtime of the simulation. 
 The maximum number of qubits on the system is 16. If the script was 
 terminated before the graph was plotted, adjust the maximum number of 
 qubits to the last system qubit count"""
for i in range(2, 17):
    try:
        state= tuple(random.choice([0, 1]) for _ in range(i))
        index1 = random.randint(0 , len(state)-2)
        index2 = index1
        while index2 == index1:
            index2 = random.randint(0, len(state)-1)
        print(f'\033[1m{len(state)}-qubit system\033[0m\nTarget qubit index: {index1}\nControl qubit index: {index2}\n')
        
        # Generate the state vector
        qc = quantumcircuit(state)
        start_time = time.time()
        qc = single_qubit_gate(qc, "X", index1)
        qc = single_qubit_gate(qc, "H", index1)
        qc = cnot_gate(qc, index1, index2)
        end_time = time.time()
        n_qubits.append(i )
        runtimes.append(end_time - start_time)
    except MemoryError:
        print(f"MemoryError encountered for {i}-qubit system")


    

plt.plot(n_qubits, runtimes, marker='o', linestyle='-')
plt.title('Simulation Runtime vs. Number of Qubits | Matrix multiplication')
plt.xlabel('Number of Qubits')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.show()
