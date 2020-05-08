from BST import BST
import random
import numpy as np

POP_SIZE = 30
GENERATIONS = 5
SELECT_PERC = 0.3

TREE_SIZE = 15

def generate_data():
    keys = [x for x in range(TREE_SIZE)]
    freqs = [x for x in range(TREE_SIZE)]
    return [x for x in zip(keys, freqs)]

def generate_population(data):
    agents = [None] * POP_SIZE
    for i in range(POP_SIZE):
        random.shuffle(data)
        agents[i] = BST(data)
    return agents

def ga():
    data = generate_data()
    agents = generate_population(data)

    for generation in range(GENERATIONS):
        print("Generation: %d Population: %d" % (generation, len(agents)))

        fitness = [- x.cost() for x in agents]

        stat = (max(fitness), np.mean(fitness), min(fitness))

        print("Best: %.2f Avg: %.2f Worst: %.2f" % stat)

def main():
    # data = generate_data()
    # # Shuffle here
    # print(data)
    # t = BST(data)
    # print(t)
    # print(t.cost())
    ga()

if __name__ == '__main__':
    main()
