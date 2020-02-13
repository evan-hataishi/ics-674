from gene import Gene
import pprint
import random

GRID_SIZE = 15
POPULATION = 100
GENERATIONS = 1000

def ga():
    agents = [Gene(GRID_SIZE) for _ in range(POPULATION)]
    for generation in range(GENERATIONS):
        print("Generation: %d Population: %d Fitness %.2f" % (generation, len(agents), min([x.get_fitness() for x in agents])))
        # fitness calculated automatically
        # selection
        next_generation = selection(agents)
        # crossover
        next_generation += crossover(agents)
        # mutation
        # print(min([x.get_fitness() for x in next_generation]))
        agents = next_generation

        best = min(agents, key=lambda x: x.get_fitness())

        pprint.pprint(best.array_representation())

        if any(agent.get_fitness() == 0 for agent in agents):
            print("Found optimal!")
            break

def selection(agents):
    agents = sorted(agents, key=lambda x: x.get_fitness())
    s = int((10*POPULATION)/100)
    return agents[:s]

def crossover(agents):
    next_generation = []
    agents = sorted(agents, key=lambda x: x.get_fitness())
    # random.shuffle(agents)
    s = int((90*POPULATION)/100)
    for _ in range(s):
        p1 = random.choice(agents[:50])
        p2 = random.choice(agents[:50])
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
