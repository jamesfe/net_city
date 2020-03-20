# -*- coding: utf-8 -*-

from blocktypes import b

defaults = {
    'link_weight': 200
}


class City:

    def __init__(self, height, width):
        self.cash = 0
        self.height = height
        self.width = width
        self.days_age = 0
        self.blocks = []
        self.horz_links = [[defaults['link_weight']] * height] * (width - 1)
        self.vert_links = [[defaults['link_weight']] * (height - 1)] * width
        print('creating a city {} wide by {} high'.format(width, height))
        print('creating horiz links with {} width and {} height'.format(len(self.horz_links[0]), len(self.horz_links)))
        print('creating vertical links with {} width and {} height'.format(len(self.vert_links[0]), len(self.vert_links)))
        for x in range(0, width):
            self.blocks.append([])
            for y in range(0, height):
                self.blocks[x].append(CityBlock(b['empty']))

    def tick(self):
        print('Tick: {}'.format(self.days_age))
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.evaluate_happiness(x, y)
                self.blocks[x][y].tick()
        self.cash += self.calculate_cashflow()
        self.days_age += 1
        self.print_status()

    def evaluate_happiness(self, x, y):
        tgt_block = self.blocks[x][y]

        if tgt_block.block_type in [b['empty'], b['industrial'], b['commercial']]:
            return 100
        if tgt_block.block_type == b['residential']:
            # First happiness is getting to and from work
            # begin a series of evaluations
            return 100
        return 100

    def calculate_cashflow(self):
        return 100

    def build_road(self, x, y, links):
        assert self.blocks[x][y].block_type == b['empty']
        self.blocks[x][y] = Road(links)
        # we should refactor this out eventually
        if links.get('north', False):
            self.vert_links[x][y - 1] = self.blocks[x][y].throughput
        if links.get('south', False):
            self.vert_links[x][y] = self.blocks[x][y].throughput
        if links.get('east', False):
            self.horz_links[x - 1][y] = self.blocks[x][y].throughput
        if links.get('west', False):
            self.horz_links[x][y] = self.blocks[x][y].throughput

    def build_res(self, x, y):
        assert self.blocks[x][y].block_type == b['empty']
        self.blocks[x, y] = CityBlock(b['residential'])

    def print_status(self):
        print('Current Cash: ${}'.format(self.cash))

    def print_city(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if x < self.width - 1:
                    print('{}--{}--'.format(self.blocks[x][y].symbol(), self.horz_links[x][y]), end='')
                if x == self.width - 1:
                    print('{}'.format(self.blocks[x][y].symbol()), end='')
            print('')
            for vl in range(0, self.width):
                if vl == 0:
                    print('  ', end='')
                if y == self.height - 1:
                    continue
                print('-{}-'.format(self.vert_links[vl][y]), end='')
            print('')


class CityBlock:

    def __init__(self, block_type):
        self.block_type = block_type
        self.level = 1
        self.simple_happiness = 100
        self.health = 100
        self.happiness = 0
        self.days_age = 0
        self.users = 0

    def symbol(self):
        typeD = {
            b['road']: 'R',
            b['residential']: 'H',
            b['empty']: '.'
        }
        return typeD.get(self.block_type, '-')

    def tick(self):
        self.days_age += 1


class Road(CityBlock):

    def __init__(self, links):
        self.links = links
        self.throughput = 100
        super().__init__(b['road'])


def main():
    city = City(3, 4)
    city.tick()
    city.tick()
    city.build_road(1, 1, {'north': True, 'West': True})
    city.tick()

    city.print_status()
    city.print_city()


if __name__ == '__main__':
    main()
