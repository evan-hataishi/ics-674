from gene import Gene
import pprint
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

GRID_SIZE = 100
POPULATION = 30
GENERATIONS = 1500

def ga():
    agents = [Gene(GRID_SIZE) for _ in range(POPULATION)]
    res = []
    for generation in range(GENERATIONS):
        print("Generation: %d Population: %d" % (generation, len(agents)))

        fitness = [- x.get_fitness() for x in agents]

        stat = (max(fitness), np.mean(fitness), min(fitness))
        res.append(stat)
        print("Best: %.2f Avg: %.2f Worst: %.2f" % stat)
        # fitness calculated automatically
        # selection
        next_generation = selection(agents)
        # crossover
        next_generation += crossover(agents)
        # print(min([x.get_fitness() for x in next_generation]))
        # mutation
        next_generation = [agent.mutate() for agent in next_generation]

        agents = next_generation

        best = min(agents, key=lambda x: x.get_fitness())

        # print(np.mean([x.get_fitness() for x in agents]))
        # pprint.pprint(best.array_representation())

        if any(agent.get_fitness() == 0 for agent in agents):
            print("Found optimal!")
            break

    # best = min(agents, key=lambda x: x.get_fitness())
    # pprint.pprint(best.array_representation())
    generations = [x for x in range(GENERATIONS)]
    data_preproc = pd.DataFrame({
        'Generation': generations,
        'Best': [x[0] for x in res],
        'Average': [x[1] for x in res],
        'Worst': [x[2] for x in res]})

    sns.lineplot(x='Generation', y='value', hue='variable',
                 data=pd.melt(data_preproc[data_preproc.index % 5 == 0], ['Generation']))
    plt.show()


def selection(agents):
    agents = sorted(agents, key=lambda x: x.get_fitness())
    s = int((10*POPULATION)/100)
    return agents[:10]

def crossover(agents):
    next_generation = []
    agents = sorted(agents, key=lambda x: x.get_fitness())
    # random.shuffle(agents)
    s = int((90*POPULATION)/100)
    for _ in range(20):
        p1 = random.choice(agents)
        p2 = random.choice(agents)
        next_generation += Gene.crossover(p1, p2)
    return next_generation

def main():
    # g = Gene(GRID_SIZE)
    # print(str(g))
    # pprint.pprint(g.array_representation())
    # pprint.pprint(g.array_representation())
    # Gene.print_grid(GRID_SIZE, g.get_path())
    # print(g.get_optimal_path())
    # Gene.print_grid(GRID_SIZE, g.get_optimal_path())
    # print(g.calc_fitness())
    ga()



if __name__ == '__main__':
    main()
