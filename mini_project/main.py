from genome import Genome
import pprint
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

GRID_SIZE = 100
POPULATION = 30
GENERATIONS = 2000
SELECT_PERC = 0.3

def ga():
    scores = []
    best = None
    average = None
    worst = None
    data = {}

    agents = [Genome(GRID_SIZE) for _ in range(POPULATION)]
    for generation in range(GENERATIONS):
        print("Genomeration: %d Population: %d" % (generation, len(agents)))

        fitness = [- x.get_fitness() for x in agents]

        stat = (max(fitness), np.mean(fitness), min(fitness))

        scores.append(stat)

        print("Best: %.2f Avg: %.2f Worst: %.2f" % stat)

        # Fitness pre-calculated adn stored in genome
        # selection
        next_generation = selection(agents)
        # crossover
        next_generation += crossover(agents)
        # mutation
        next_generation = [agent.mutate() for agent in next_generation]

        agents = sorted(next_generation, key=lambda x: x.get_fitness())

        best = agents[0]
        average = agents[int(POPULATION/2)]
        worst = agents[-1]

        # print(np.mean([x.get_fitness() for x in agents]))
        # pprint.pprint(best.array_representation())

        if best.get_fitness() == 0:
            print("Found optimal!")
            break

    # best = min(agents, key=lambda x: x.get_fitness())
    # pprint.pprint(best.array_representation())
    generations = [x for x in range(GENERATIONS)]
    data_preproc = pd.DataFrame({
        'Generation': generations,
        'Best': [x[0] for x in scores],
        'Average': [x[1] for x in scores],
        'Worst': [x[2] for x in scores]})

    sns.lineplot(x='Generation', y='value', hue='variable',
                 data=pd.melt(data_preproc[data_preproc.index % 5 == 0], ['Generation']))
    plt.show()

    data['scores'] = scores
    data['best'] = best.array_representation()
    data['average'] = average.array_representation()
    data['worst'] = worst.array_representation()

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def selection(agents):
    agents = sorted(agents, key=lambda x: x.get_fitness())
    s = int(SELECT_PERC*POPULATION)
    return agents[:s]

def crossover(agents):
    next_generation = []
    agents = sorted(agents, key=lambda x: x.get_fitness())
    # random.shuffle(agents)
    s = int((1-SELECT_PERC)*POPULATION)
    for _ in range(s):
        p1 = random.choice(agents)
        p2 = random.choice(agents)
        next_generation += Genome.crossover(p1, p2)
    return next_generation

def main():
    ga()

if __name__ == '__main__':
    main()
