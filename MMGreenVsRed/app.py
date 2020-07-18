RED_TO_GREEN = [3, 6]
GREEN_TO_GREEN = [2, 3, 6]


def is_green(obj):
    return obj.get_data() == '1'


# TODO Utility class
class Cell:

    def __init__(self, cell_row, cell_col, cell_data):
        self.__row = cell_row
        self.__col = cell_col
        self.__data = cell_data

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__col

    def count_green_neighbours(self, grid):
        neighbours = 0
        if self.__col - 1 >= 0:
            if is_green(grid[self.__row][self.__col - 1]):
                neighbours = neighbours + 1
        if self.__col - 1 >= 0 and self.__row - 1 >= 0:
            if is_green(grid[self.__row - 1][self.__col - 1]):
                neighbours = neighbours + 1
        if self.__row - 1 >= 0:
            if is_green(grid[self.__row - 1][self.__col]):
                neighbours = neighbours + 1
        if self.__col + 1 != len(grid[0]) and self.__row - 1 >= 0:
            if is_green(grid[self.__row - 1][self.__col + 1]):
                neighbours = neighbours + 1
        if self.__col + 1 != len(grid[0]):
            if is_green(grid[self.__row][self.__col + 1]):
                neighbours = neighbours + 1
        if self.__col + 1 != len(grid[0]) and self.__row + 1 != len(grid):
            if is_green(grid[self.__row + 1][self.__col + 1]):
                neighbours = neighbours + 1
        if self.__row + 1 != len(grid):
            if is_green(grid[self.__row + 1][self.__col]):
                neighbours = neighbours + 1
        if self.__col - 1 >= 0 and self.__row + 1 != len(grid):
            if is_green(grid[self.__row + 1][self.__col - 1]):
                neighbours = neighbours + 1
        return neighbours


# Getting the dimensions of the grid
dimensions = input().split(", ")
columns = int(dimensions[0])
rows = int(dimensions[1])

if rows < 1000 and columns < 1000:
    # Filling the Generation Zero to the grid of objects
    old_generation = [[Cell(0, 0, '') for _ in range(rows)] for _ in range(columns)]
    for row in range(rows):
        line = [x for x in list(input())]
        for column in range(len(line)):
            old_generation[row][column] = Cell(row, column, line[column])

    # Getting the coordinates of the observed cell and the number of generations to be observed
    coordinates_and_generations = input().split(", ")
    generations_to_observe = int(coordinates_and_generations[2])
    cell_to_observe_r = int(coordinates_and_generations[1])
    cell_to_observe_c = int(coordinates_and_generations[0])

    result = 0
    # Start of the game
    for _ in range(generations_to_observe):
        new_generation = [[Cell(0, 0, '') for _ in range(rows)] for _ in range(columns)]

        for r in range(rows):
            for c in range(columns):

                # Counting the number of green neighbour cells
                green_neighbours = old_generation[r][c].count_green_neighbours(old_generation)

                # Checking for the colour of the cell and if the cell
                # is green and is the observed one, incrementing result
                if old_generation[r][c].get_data() == '0':
                    if green_neighbours in RED_TO_GREEN:
                        new_generation[r][c] = Cell(r, c, '1')
                        if r == cell_to_observe_r and c == cell_to_observe_c:
                            result = result + 1
                    else:
                        new_generation[r][c] = Cell(r, c, '0')
                else:
                    if green_neighbours in GREEN_TO_GREEN:
                        new_generation[r][c] = Cell(r, c, '1')
                        if r == cell_to_observe_r and c == cell_to_observe_c:
                            result = result + 1
                    else:
                        new_generation[r][c] = Cell(r, c, '0')
        # The new generation becomes old generation
        old_generation = new_generation
    print("Result: {}".format(result))
