# -*- coding: utf-8 -*-

EMPTY = 1
RESIDENTIAL = 2
COMMERCIAL = 3
INDUSTRIAL = 4


class City:

    def __init__(self, height, width):
        self.cash = 0
        self.height = height
        self.width = width
        self.days_age = 0
        self.blocks = []
        self.horz_links = [[200] * height] * (width - 1)
        self.vert_links = [[200] * width] * (height - 1)
        for x in range(0, width):
            self.blocks.append([])
            for y in range(0, height):
                self.blocks[x].append(CityBlock(EMPTY))

    def tick(self):
        print('Tick: {}'.format(self.days_age))
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.evaluate_happiness(x, y)
        self.cash += self.calculate_cashflow()
        self.days_age += 1
        self.print_status()

    def evaluate_happiness(self, x, y):
        return 100

    def calculate_cashflow(self):
        return 100

    def print_status(self):
        print('Current Cash: ${}'.format(self.cash))


class CityBlock:

    def __init__(self, block_type):
        self.block_type = block_type
        self.health = 100
        self.happiness = 0
        self.days_age = 0


def main():
    city = City(3, 3)
    city.tick()
    city.tick()
    city.tick()

    city.print_status()


if __name__ == '__main__':
    main()
