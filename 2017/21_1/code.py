""" Advent of code 2017 day 21/1 """
from argparse import ArgumentParser
import re
import numpy

class Pattern(object):
    """Particle representation"""
    def __init__(self, representation, pattern, result):
        """Constructor"""
        self.repr = representation
        self.matchers = self.transform_pattern(pattern)
        self.result = result

    @classmethod
    def transform_pattern(cls, pattern):
        """ Flip, rotate the elements """
        newpatterns = set()
        current = pattern
        for rotate in range(4):
            newpatterns.add(current)
            vert = cls.flip_v(current)
            newpatterns.add(vert)
            newpatterns.add(cls.flip_h(current))
            newpatterns.add(cls.flip_h(vert))
            current = cls.rotate(current, rotate)
        return newpatterns

    def __repr__(self):
        """ Representation of the pattern """
        return self.repr

    @staticmethod
    def flip_h(pattern):
        """ Flip horizontally """
        return '/'.join([line[::-1] for line in pattern.split('/')])

    @staticmethod
    def flip_v(pattern):
        """ Flip vertically """
        return '/'.join([''.join(line) for line in pattern.split('/')[::-1]])

    @staticmethod
    def rotate(pattern, rot):
        """ Rotate counterclockwise rot*90 degrees """
        rotated = numpy.rot90([[char for char in line] for line in pattern.split('/')], rot)
        return '/'.join([''.join(line) for line in rotated])

class Fractal(object):
    """ Fractal representation """
    def __init__(self, data):
        """Constructor"""
        self.patterns = self.read_data(data)
        self.start = ".#./..#/###"
        self.image = self.deflatten(self.start)
        self.size = 3

    def __repr__(self):
        """ representation of the fractal """
        return "Fractal({})".format(self.size)

    @classmethod
    def read_data(cls, data):
        """ Read the data from the input """
        pattern = re.compile(r'([.#/]+) => ([.#/]+)')
        matchers = dict()
        for line in data.split('\n'):
            new_matchers = cls.parse_line(pattern, line)
            #key_new = set(new_matchers.keys())
            #key_old = set(matchers.keys())
            #print("already existing keys: ", len(key_new.intersection(key_old)))
            matchers.update(new_matchers)
        return matchers

    @staticmethod
    def parse_line(pattern, line):
        """ Apply regexp to line to get the specific data """
        groups = re.match(pattern, line)
        which = Pattern(line, groups.group(1), groups.group(2))
        return {match: which for match in which.matchers}

    @property
    def lighted(self):
        """ Return the string version of the position """
        return numpy.count_nonzero(self.image == '#')

    def break_image(self, break_count):
        """ Break the images into n parts"""
        array = numpy.reshape(self.image, (self.size, self.size))
        return self.blockshaped(array, break_count, break_count)

    def update(self, break_count, fragments):
        """ Update all the fragments with the matching rules """
        image = []
        newsize = (3 if break_count == 2 else 4)
        print("update image of size:{} to newsize:{}".format(self.size, newsize))
        for frag in fragments:
            flattened = self.flatten(frag)
            print(" frag: {}".format(flattened))
            if flattened not in self.patterns:
                raise Exception('Pattern missing!')
            newpattern = self.patterns[flattened].result
            print("  into: {}".format(newpattern))
            array = numpy.reshape(self.deflatten(newpattern), (newsize, newsize))
            image.append(array.copy())
        separated_count = self.size // break_count
        size = separated_count * newsize
        separated = list(self.chunks(image, separated_count))
        updated = self.unblockshaped(separated)
        return updated, size

    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def flatten(matrix):
        """ Create enchantment rule from submatrix """
        return '/'.join([''.join(line) for line in matrix])

    @staticmethod
    def deflatten(string):
        """ Create submatrix rule from enchantment """
        return [[char for char in line] for line in string.split('/')]

    @staticmethod
    def blockshaped(arr, nrows, ncols):
        """
        Return an array of shape (n, nrows, ncols) where
        n * nrows * ncols = arr.size

        If arr is a 2D array, the returned array should look like n subblocks with
        each subblock preserving the "physical" layout of arr.
        """
        height, _ = arr.shape
        return (arr.reshape(height//nrows, nrows, -1, ncols)
                .swapaxes(1, 2)
                .reshape(-1, nrows, ncols))

    @staticmethod
    def unblockshaped(arr):
        """ Rearrange the arrays """
        return numpy.block(arr)

    def simulate(self, count):
        """ Simulate the image manipulation

        If the size is evenly divisible by 2,
        break the pixels up into 2x2 squares,
        and convert each 2x2 square into a 3x3 square
        by following the corresponding enhancement rule.

        Otherwise, the size is evenly divisible by 3;
        break the pixels up into 3x3 squares,
        and convert each 3x3 square into a 4x4 square
        by following the corresponding enhancement rule."""
        for _ in range(count):
            break_count = 2 if self.size%2 == 0 else 3
            self.image, self.size = self.update(break_count, self.break_image(break_count))
            print(self.size)
            print(self.flatten(self.image))

def solution(data, count):
    """ Solution to the problem """
    fractal = Fractal(data)
    fractal.simulate(count)
    return fractal.lighted

if __name__ == "__main__":
    PARSER = ArgumentParser()
    PARSER.add_argument("--input", dest='input', action='store_true')
    PARSER.add_argument("--test")
    ARGS = PARSER.parse_args()
    if ARGS.input:
        with(open('input.txt', 'r')) as input_file:
            print(solution(input_file.read(), 5))
    elif ARGS.test:
        print(solution(str(ARGS.test), 2))
    else:
        DEBUG = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""
        print(solution(DEBUG, 2))
