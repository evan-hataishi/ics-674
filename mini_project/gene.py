import random

class Gene():

    # right, up, diagonal, none
    moves = ('R', 'U', 'D', None)

    __grid_size = 0
    __path_length = 0
    __path = None

    def __init__(self, GRID_SIZE):
        self.__grid_size  = GRID_SIZE
        self.__path_length = (GRID_SIZE - 1) * 2
        self.__path = [random.choice(self.moves) for _ in range(self.__path_length)]
        self.__path = Gene.restrict_path(self.__path)
        # self.__optimal_path = ['D' for _ range(self.__path_length)]
        self.__fitness = -1


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
        return Gene.__fill_rest(path, grid_size, step, x_pos, y_pos)

    @staticmethod
    def __fill_rest(path, grid_size, step, x_pos, y_pos):
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


    # def fitness(self):


    def get_path(self):
        return self.__path
