from BST import BST
from BST import optBSTCost
import random
import numpy as np

POP_SIZE = 45
GENERATIONS = 500
SELECT_PERC = 0.3

TREE_SIZE = 50

def generate_data():
    keys = [x for x in range(TREE_SIZE)]
    random.shuffle(keys)
    freqs = [random.randint(1, 10) for x in range(TREE_SIZE)]
    return [x for x in zip(keys, freqs)]

def generate_population(data):
    agents = [None] * POP_SIZE
    for i in range(POP_SIZE):
        random.shuffle(data)
        agents[i] = BST(data)
    return agents

def selection(agents):
    s = int(SELECT_PERC*POP_SIZE)
    return agents[:s]

def crossover(agents):
    next_generation = []
    # random.shuffle(agents)
    s = int((1-SELECT_PERC)*POP_SIZE)
    for _ in range(s):
        p1 = random.choice(agents)
        p2 = random.choice(agents)
        next_generation.append(BST.crossover(p1, p2))
    return next_generation

def ga():
    data = generate_data()
    agents = generate_population(data)

    optimal_cost = optBSTCost([x[0] for x in data], [x[1] for x in data], len(data))

    for generation in range(GENERATIONS):
        print("Generation: %d Population: %d" % (generation, len(agents)))

        fitness = [- x.cost() for x in agents]

        stat = (max(fitness), np.mean(fitness), min(fitness))

        print("Best: %.2f Avg: %.2f Worst: %.2f" % stat)

        agents = sorted(agents, key=lambda x: x.cost())

        # selection
        next_generation = selection(agents)

        # crossover
        next_generation += crossover(agents)

        # mutation
        next_generation = [agent.mutate() for agent in next_generation]

        agents = next_generation

    print("Optimal BST Cost: %d" % optimal_cost)


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
