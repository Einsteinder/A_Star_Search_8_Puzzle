import queue as Q

HEURISTIC = 'manhattan_distance' # LINE 33 use this constant
#HEURISTIC = 'misplaced_tiles'

class Node:
    def __init__(self, state, parent=-1, gn=0):
        self.state = state
        self.gn = gn
        self.hn = self.cost
        self.fn = self.gn + self.hn
        self.parent = parent

    def __str__(self):
        return self.state

    def __repr__(self):
        return self.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return int(self.state)

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise "Can not compare Node with other type of object"
        return self.fn < other.fn

    @property
    def cost(self):
        return getattr(self, HEURISTIC)()

    def misplaced_tiles(self):

        i = 0
        distance = 0
        while i < (len(self.state)):


            n = int(self.state[i]) - 1
            if (n + 1) == 0:
                i += 1;continue
            n = n + 1
            if n != i:

                distance = distance + i
            i += 1


        return distance

    def manhattan_distance(self):
        distance = 0
        row_len = 3
        i = 0
        while i < (len(self.state)):

            n = int(self.state[i]) - 1
            if (n + 1) == 0:
                i += 1;continue
            n = n + 1
            x1, y1 = (n % row_len), int(n / row_len)
            x2, y2 = (i % row_len), int(i / row_len)

            x = x2 - x1
            y = y2 - y1

            distance = distance + abs(x) + abs(y)
            i += 1
        return distance

    @property
    def neighbours(self):

        def swap(s, i, j):
            lst = list(s);
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)

        def range_check(index, start=0, end=8):
            if index >= start and index <= end:
                return 1
            return 0

        index = list(self.state).index('0')

        row_len = 3
        row_start = 0
        remainder = index % row_len
        tmp = []

        right = (index + 1) if remainder + 1 < row_len else None  
        left = (index - 1) if remainder - 1 >= row_start else None
        top = (index - row_len) if range_check(index - row_len) else None
        bottom = (index + row_len) if range_check(index + row_len) else None

   

        tmp.append(top) if top is not None else None
        tmp.append(bottom) if bottom is not None else None
        tmp.append(right) if right is not None else None
        tmp.append(left) if left is not None else None

        new_neighbours = []
        for move_to_index in tmp:
            new_neighbours.append(
                Node(
                    swap(self.state, index, move_to_index), self, self.gn + 1
                )
            )
        return new_neighbours

    def print_node(self):

        print('********')
        print(self.state[0], ' ', self.state[1], ' ', self.state[2])
        print(self.state[3], ' ', self.state[4], ' ', self.state[5])
        print(self.state[6], ' ', self.state[7], ' ', self.state[8])
        print('********')
        print(self.fn, '=', self.hn, '+', self.gn)

    def print_path(self):
        node = self
        while node != -1:
            node.print_node()
            node = node.parent

def a_star(node, goal):
    open_list = Q.PriorityQueue()
    close_list = []
    moves_counter = 0
    max_move_counter = 9999
    while True:
        if max_move_counter == moves_counter:
            print('EXCEEDED MAX MOVES')
            return
        moves_counter += 1

        #add node to explored set
        for neighbour in (list(set(node.neighbours) - set(close_list))):
            open_list.put(neighbour)

        node = open_list.get()
        #node.print_node()

        if node == goal:
            print('Moves = ', moves_counter)
            print('Explored Nodes = ', len(open_list.queue) + len(close_list))

            return

        close_list.append(node)

a_star(Node('724506831'), Node('012345678'))
#a_star(Node('102345678'), Node('012345678'))

