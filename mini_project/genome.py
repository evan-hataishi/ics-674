import random
import pprint
from math import sqrt

class Genome():

    # right, up, diagonal, none
    moves = ('R', 'U', 'D', None)

    __grid_size  = None
    __path_length = None
    __path = None
    __optimal_path = None
    __optimal_path_points = None
    __fitness = None


    def __init__(self, GRID_SIZE, path=None):
        self.__grid_size  = GRID_SIZE
        self.__path_length = (GRID_SIZE - 1) * 2
        self.__path = Genome.restrict_path(path) if path else self.__random_path()
        self.__optimal_path = self.__find_optimal_path()
        self.__optimal_path_points = self.__find_optimal_path_points()
        self.__fitness = self.calc_fitness()


    def __str__(self):
        return "Path: " + str(self.__path) + "\nFitness: " + str(self.__fitness)


    def array_representation(self):
        grid = [['_' for _ in range(self.__grid_size)] for _ in range(self.__grid_size)]
        x_pos, y_pos = 0, 0
        grid[len(grid[0]) - 1 - y_pos][x_pos] = 'X'
        for i in range(self.__path_length):
            if self.__path[i] == 'R':
                x_pos += 1
            elif self.__path[i] == 'U':
                y_pos += 1
            elif self.__path[i] == 'D':
                x_pos += 1
                y_pos += 1
            # print(x_pos, y_pos)
            grid[len(grid[0]) - 1 - y_pos][x_pos] = 'X'
        return grid


    @staticmethod
    def print_grid(grid_size, path):
        grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]
        x_pos, y_pos = 0, 0
        grid[len(grid[0]) - 1 - y_pos][x_pos] = 'X'
        for i in range(len(path)):
            if path[i] == 'R':
                x_pos += 1
            elif path[i] == 'U':
                y_pos += 1
            elif path[i] == 'D':
                x_pos += 1
                y_pos += 1
            # print(x_pos, y_pos)
            grid[len(grid[0]) - 1 - y_pos][x_pos] = 'X'
        pprint.pprint(grid)


    # It's annoying that I have to check everything before...
    @staticmethod
    def restrict_path(path):
        grid_size = (len(path) // 2) + 1
        step, x_pos, y_pos = 0, 0, 0
        while (step < len(path)) and (x_pos < grid_size) and (y_pos < grid_size):
            if path[step] == 'R' and (x_pos + 1 < grid_size):
                x_pos += 1
            elif path[step] == 'U' and (y_pos + 1 < grid_size):
                y_pos += 1
            elif path[step] == 'D' and (x_pos + 1 < grid_size) and (y_pos + 1 < grid_size):
                x_pos += 1
                y_pos += 1
            elif path[step] == None:
                # Don't move
                pass
            else:
                # This step will take us out of the grid. Break out of loop here.
                break
            step += 1
        return Genome.__fill_path(path, grid_size, step, x_pos, y_pos)


    @staticmethod
    def __fill_path(path, grid_size, step, x_pos, y_pos):
        while (step < len(path)) and (x_pos < grid_size - 1):
            path[step] = 'R'
            x_pos += 1
            step += 1
        while (step < len(path)) and (y_pos < grid_size - 1):
            path[step] = 'U'
            y_pos += 1
            step += 1
        for i in range(step, len(path)):
            path[i] = None
        return path


    def calc_fitness(self):
        curr_x, curr_y = 0, 0
        fitness = 0
        for i in range(self.__path_length):
            move = self.__path[i]
            if move == 'R' or move == 'D':
                curr_x += 1
            if move == 'U' or move == 'D':
                curr_y += 1
            dist = Genome.__distance((curr_x, curr_y), self.__optimal_path_points[i])
            fitness += dist
            # print(dist, (curr_x, curr_y), self.__optimal_path_points[i])
        return fitness


    @staticmethod
    def __distance(a, b):
        return sqrt((b[1] - a[1])**2 + (b[0] - a[0])**2)


    def __random_path(self):
        path = [random.choice(self.moves) for _ in range(self.__path_length)]
        return Genome.restrict_path(path)


    def __find_optimal_path(self):
        optimal_path = [None for _ in range(self.__path_length)]
        for i in range(self.__grid_size - 1):
            optimal_path[i] = 'D'
        return optimal_path


    def __find_optimal_path_points(self):
        final_pos = (self.__grid_size - 1, self.__grid_size - 1)
        optimal_path = [final_pos for _ in range(self.__path_length)]
        for i in range(self.__grid_size - 1):
            optimal_path[i] = (i + 1, i + 1)
        return optimal_path


    def get_path(self):
        return self.__path


    def get_path_length(self):
        return self.__path_length


    def get_optimal_path(self):
        return self.__optimal_path


    def get_optimal_path_points(self):
        return self.__optimal_path_points


    def get_fitness(self):
        return self.__fitness


    @staticmethod
    def crossover(p1, p2):
        length = min(p1.get_path_length(), p2.get_path_length())
        # split = random.randint(0, length)
        # c1_path = p1.get_path()[0:split] + p2.get_path()[split:length]
        # c2_path = p2.get_path()[0:split] + p1.get_path()[split:length]
        child_path = []
        for i in range(length):
            child_path.append(random.choice([p1.get_path()[i], p2.get_path()[i]]))
        grid_size = (length // 2) + 1
        # return [Genome(grid_size, c1_path), Genome(grid_size, c2_path)]
        return [Genome(grid_size, child_path)]

    def mutate(self):
        prob = random.uniform(0,1)
        if prob <= 0.1:
            self.__path = self.__random_path()
            self.__fitness = self.calc_fitness()
        return self
