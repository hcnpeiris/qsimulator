from quantumtools.tensorsim import quantumcircuit, cnot_gate, single_qubit_gate
import random, time
import matplotlib.pyplot as plt

n_qubits = []
runtimes = []

""" Plots the runtime of the simulation. 
 The maximum number of qubits on the system is 29. If the script was 
 terminated before the graph was plotted, adjust the maximum number of 
 qubits to the last system qubit count"""

for i in range(2,30):
    state= tuple(random.choice([0, 1]) for _ in range(i))
    index1 = random.randint(0 , len(state)-2)
    index2 = random.randint(0, len(state) - 1)
    while index2 == index1:
        index2 = random.randint(0, len(state) - 1)
    print(f'\033[1m{len(state)}-qubit system\033[0m\nTarget qubit index: {index1}\nControl qubit index: {index2}\n')
    

    state_vec = quantumcircuit(state)
    start_time = time.time()
    state_vec1 = single_qubit_gate(state_vec, 'X',index1)
    state_vec2 = single_qubit_gate(state_vec1, 'H',index1)
    state_vec3 = cnot_gate(state_vec2, index1, index2)
    end_time = time.time()
    n_qubits.append(i )
    runtimes.append(end_time - start_time)

plt.plot(n_qubits, runtimes, marker='o', linestyle='-')
plt.title('Simulation Runtime vs. Number of Qubits | Tensor multiplication')
plt.xlabel('Number of Qubits')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.show()