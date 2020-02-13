from gene import Gene
import pprint

GRID_SIZE = 5

def main():
    g = Gene(GRID_SIZE)
    print(str(g))
    pprint.pprint(g.array_representation())

if __name__ == '__main__':
    main()
