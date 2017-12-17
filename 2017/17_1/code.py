""" Advent of code 2017 day 17/1 """
from argparse import ArgumentParser

class Node(object):
    """ Node that contains the data for linked list """
    def __init__(self, data):
        """ Constructor with data and next element """
        self.data = data
        self.next = None

    def __repr__(self):
        #next_data = self.next
        next_data = self.next.data if self.next is not None else None
        return "{}, {}".format(self.data, next_data)

class Linkedlist(object):
    """ Linked list that can be traversed around and add new nodes easily """
    def __init__(self):
        """ Constructor """
        self.start_node = None
        self.cur_node = None
        self.length = 0
        self.cur_pos = -1

    def __repr__(self):
        """ Representation of the linked list """
        return "LinkedList([{}],{}/{})".format(self.cur_node, self.cur_pos, self.length)

    def add_node(self, data):
        """ Insert a new node into the linked list """
        new_node = Node(data)
        if self.cur_node is not None:
            new_node.next, self.cur_node.next = self.cur_node.next, new_node
        self.cur_node = new_node
        self.length += 1
        self.cur_pos += 1
        if self.start_node is None:
            self.start_node = self.cur_node
        # print("Node({}) added to {}".format(new_node.data, self.cur_pos-1))

    def list_print(self):
        """ Print the linked list """
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.next

    def move_circular(self, count):
        """ Move in the linked list n places, if reached the end start from the start"""
        planned_move = self.cur_pos + count
        if count + planned_move < self.length:
            move_count = count
            self.cur_pos += move_count
            # print("Move less from {} to {}({})".format(
            #   self.cur_pos,
            #   self.cur_pos + move_count,
            #   planned_move
            # ))
        else:
            self.cur_node = self.start_node
            move_count = max(0, (planned_move % (self.length)))
            # print("Move circ from {} to {}({})".format(self.cur_pos, move_count, planned_move))
            self.cur_pos = move_count
        for _ in range(move_count):
            self.cur_node = self.cur_node.next

    def get_next(self):
        """ Get the data of the next node"""
        return self.cur_node.next.data

class Spinlock(object):
    """ Spinlock implementation """
    def __init__(self, init):
        """Constructor for the twister """
        self.stepforward = int(init)
        self.data = Linkedlist()

    def __repr__(self):
        """Representation of the spinlock """
        return "Spinlock({})".format(self.stepforward)

    def process(self, count):
        """ Move n steps then insert a new value """
        self.data.add_node(0)
        for index in range(1, count + 1):
            # print("{}.: {}".format(index, self.data))
            self.data.move_circular(self.stepforward)
            self.data.add_node(index)
        return self.data.get_next()

def solution(data):
    """ Solution to the problem """
    lock = Spinlock(data)
    return lock.process(2017)

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
        DEBUG = """3"""
        print(solution(DEBUG))
