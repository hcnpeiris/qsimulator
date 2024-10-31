import matplotlib.pyplot as plt
from collections import Counter


def histogram(data):
    counts = Counter(data)
    total = sum(counts.values())


    labels = list(counts.keys())
    probabilities = [value / total for value in counts.values()]

    plt.bar(labels, probabilities)
    plt.xlabel('State')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Quantum States')
    plt.xticks(rotation=45)  
    plt.show()
