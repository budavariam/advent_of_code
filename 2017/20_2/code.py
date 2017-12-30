""" Advent of code 2017 day 20/2 """
from argparse import ArgumentParser
from collections import defaultdict
from functools import reduce
import re

class Particle(object):
    """Particle representation"""
    def __init__(self, number, data):
        """Constructor"""
        self.position = data['p']
        self.acceleration = data['a']
        self.velocity = data['v']
        self.number = number
        self.distance = self.calc_distance(self.position)
        #print("{}. [{}]".format(self.number, ','.join(map(str, self.position))))

    def update(self):
        """ Update the particle data """
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]
        self.distance = self.calc_distance(self.position)
        #print("{}. [{}]".format(self.number, ','.join(map(str, self.position))))
        return True

    @property
    def pos(self):
        """ Return the string version of the position """
        return ','.join(map(str, self.position))

    @staticmethod
    def calc_distance(position):
        """ Get the distance of the particle """
        return reduce(lambda acc, pos: acc + abs(pos), position, 0)

    def __repr__(self):
        """ Representation of the particle """
        return "Partice #{}".format(self.number)

class Swarm(object):
    """ Swarm representation """
    def __init__(self, data):
        """Constructor"""
        self.particles = {elem[0]: Particle(*elem) for elem in enumerate(self.read_data(data))}

    @property
    def particlecount(self):
        """ Return the string version of the position """
        return len(self.particles)

    @staticmethod
    def parse_line(pattern, line):
        """ Apply regexp to line to get the specific data """
        groups = re.match(pattern, line)
        result = dict()
        result['p'] = [int(elem) for elem in groups.group(1).split(",")]
        result['v'] = [int(elem) for elem in groups.group(2).split(",")]
        result['a'] = [int(elem) for elem in groups.group(3).split(",")]
        return result

    @classmethod
    def read_data(cls, data):
        """ Read the data from the input """
        pattern = re.compile(r'p=<(.*?)>, v=<(.*?)>, a=<(.*?)>')
        return [cls.parse_line(pattern, line) for line in data.split('\n')]

    def simulate(self, steps):
        """ Update the particles """
        for step in range(steps):
            if step % 100 == 0:
                print(step, self.particlecount)
            for _, particle in self.particles.items():
                particle.update()
            self.remove_collisions()

    def closest(self):
        """ Get the closest particle, so the one with the mimimum distance """
        return min(self.particles.items(), key=lambda x: x[1].distance)[0]

    def remove_collisions(self):
        """ If the positions are the same then remove the particles from the data dict """
        positions = defaultdict(list)
        removables = set([])
        for index, particle in self.particles.items():
            positions[particle.pos].append(index)
            length = len(positions[particle.pos])
            if length == 2:
                removables.add(positions[particle.pos][0])
            if length > 1:
                removables.add(index)
        for key in removables:
            if key in self.particles:
                del self.particles[key]

def solution(data):
    """ Solution to the problem """
    swarm = Swarm(data)
    swarm.simulate(1000)
    return swarm.particlecount

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read()))
    elif ARGS.test:
        print(solution(str(ARGS.test)))
    else:
        DEBUG = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"""
        print(solution(DEBUG))
