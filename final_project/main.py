from BST import BST
from BST import optBSTCost
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

POP_SIZE = 45
GENERATIONS = 300
SELECT_PERC = 0.3

TREE_SIZE = 100

def generate_data():
    keys = [x for x in range(TREE_SIZE)]
    random.shuffle(keys)
    freqs = [random.randint(0, 10) for x in range(TREE_SIZE)]
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

    scores = []
    best = None
    average = None
    worst = None
    data = {}

    for generation in range(GENERATIONS):
        print("Generation: %d Population: %d" % (generation, len(agents)))

        fitness = [- x.cost() for x in agents]

        stat = (max(fitness), np.mean(fitness), min(fitness))

        scores.append(stat)

        print("Best: %.2f Avg: %.2f Worst: %.2f" % stat)

        agents = sorted(agents, key=lambda x: x.cost())

        # selection
        next_generation = selection(agents)

        # crossover
        next_generation += crossover(agents)

        # mutation
        next_generation = [agent.mutate() for agent in next_generation]

        agents = sorted(next_generation, key=lambda x: x.cost())

        # best = agents[0]
        # average = agents[int(POP_SIZE/2)]
        # worst = agents[-1]

    print("Optimal BST Cost: %d" % optimal_cost)

    # Display plot
    # generations = [x for x in range(GENERATIONS)]
    # data_preproc = pd.DataFrame({
    #     'Generation': generations,
    #     'Optimal': [- optimal_cost for x in scores],
    #     'Best': [x[0] for x in scores],
    #     'Average': [x[1] for x in scores],
    #     'Worst': [x[2] for x in scores]})
    #
    # sns.lineplot(x='Generation', y='value', hue='variable',
    #              data=pd.melt(data_preproc, ['Generation']))
    # plt.show()

    # Save data to json
    # data['scores'] = scores
    # data['optimal'] = optimal_cost
    #
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

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
