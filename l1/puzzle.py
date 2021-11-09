from heapq import heappush, heappop, heapify
from enum import Enum
import random


class State:
    """
    The class represents the single node
    """
    def __init__(self, state, parent, move, g, cost, key):
        self.state = state
        self.parent = parent
        self.move = move  # Direction - skąd przyszliśmy do tego stanu, jaki ruch wcześniej wykonaliśmy
        self.g = g  # depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(hex(e)[2:]) for e in self.state)

    def __eq__(self, other):
        """
        The method check is node's map is equal with other
        :param other: the other nodes map
        :return: True if equal, False otherwise
        """
        return self.map == other.map

    def __lt__(self, other):
        """
        The method check is node's map is less than other
        :param other: the other nodes map
        :return: True if less than, False otherwise
        """
        return self.map < other.map


class Direction(Enum):
    """
    The enumerate class represents direction we want to move
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Puzzle:
    def __init__(self, n):
        self.size = n
        self.finishState = [i + 1 for i in range(self.size ** 2)]
        self.finishState[self.size ** 2 - 1] = 0
        self.nodesExpanded = 0

    def showState(self, board):
        """
        The method prints board as friendly way for eyes.
        :param board: Array - represents a currern board which we want to print
        """
        for i in range(len(board)):
            print(board[i], end=" ")
            if i % self.size == (self.size - 1):
                print("")

    def move(self, state, direction):
        """
        The method moves available movement in direction
        :param state: current state
        :param direction: direction which we want to move
        :return: new state after moved or None if movement is not available
        """
        newState = list(state)
        blankIdx = newState.index(0)

        if direction == Direction.UP:
            if blankIdx - self.size > 0:
                newState[blankIdx - self.size], newState[blankIdx] = newState[blankIdx], newState[blankIdx - self.size]
                return newState
            else:
                return None

        if direction == Direction.DOWN:
            if blankIdx + self.size < self.size ** 2:
                newState[blankIdx + self.size], newState[blankIdx] = newState[blankIdx], newState[blankIdx + self.size]
                return newState
            else:
                return None

        if direction == Direction.LEFT:
            if blankIdx % self.size != 0:
                newState[blankIdx - 1], newState[blankIdx] = newState[blankIdx], newState[blankIdx - 1]
                return newState
            else:
                return None

        if direction == Direction.RIGHT:
            if blankIdx % self.size != (self.size - 1):
                newState[blankIdx + 1], newState[blankIdx] = newState[blankIdx], newState[blankIdx + 1]
                return newState
            else:
                return None

    def countUnplacedHeuristic(self, state):
        """
        The method counts how many puzzle is not placed.
        :param state: array represents current state
        :return: the cost of heuristic
        """
        unplaced = 0
        for i in range(len(state)):
            if state[i] != self.finishState[i]:
                unplaced += 1
        return unplaced

    def countManhattanHeuristic(self, state):
        """
        The method counts how many steps for each puzzle is to gain final state
        The Manhattan heuristic
        :param state: array represents current state
        :return: the cost of heuristic
        """
        count = 0

        for i in range(1, len(state)):
            tmp = abs(state.index(i) % self.size - self.finishState.index(i) % self.size) + \
                  abs(state.index(i) // self.size - self.finishState.index(i) // self.size)
            count += tmp

        return count

    def expand(self, node):
        """
        The method expands state in each direction
        :param node: Current node
        :return: return list of neighbor
        """
        neighbors = list()
        self.nodesExpanded += 1

        neighbors.append(
            State(self.move(node.state, Direction.UP), node, Direction.UP, node.g + 1, node.cost + 1, 0))
        neighbors.append(
            State(self.move(node.state, Direction.DOWN), node, Direction.DOWN, node.g + 1, node.cost + 1, 0))
        neighbors.append(
            State(self.move(node.state, Direction.LEFT), node, Direction.LEFT, node.g + 1, node.cost + 1, 0))
        neighbors.append(
            State(self.move(node.state, Direction.RIGHT), node, Direction.RIGHT, node.g + 1, node.cost + 1, 0))

        return [neighbor for neighbor in neighbors if neighbor.state]

    def astar(self, startState, heuristic):
        """
        The method runs solver using a * algorithms with heuristic
        :param startState: initial state
        :param heuristic: "manhattan" - uses manhattan heuristic, "unplaced" uses unplaced heuristic
        :return: the node with state equals final state
        """
        heap = list()
        heapentry = dict()
        explored = set()

        if heuristic == "manhattan":
            key = self.countManhattanHeuristic(startState)
        elif heuristic == "unplaced":
            key = self.countUnplacedHeuristic(startState)
        else:
            return None

        root = State(state=startState, parent=None, move=None, g=0, cost=0, key=key)
        entry = (key, 0, root)
        heappush(heap, entry)
        heapentry[root.map] = entry

        while heap:
            node = heappop(heap)
            explored.add(node[2].map)

            if node[2].state == self.finishState:
                print("Finish")
                return node[2]

            neighbors = self.expand(node[2])

            for neighbor in neighbors:
                if heuristic == "manhattan":
                    neighbor.key = neighbor.cost + self.countManhattanHeuristic(neighbor.state)
                elif heuristic == "unplaced":
                    neighbor.key = neighbor.cost + self.countUnplacedHeuristic(neighbor.state)
                else:
                    return None

                entry = (neighbor.key, neighbor.move.value, neighbor)

                if neighbor.map not in explored:
                    heappush(heap, entry)
                    explored.add(neighbor.map)
                    heapentry[neighbor.map] = entry

                elif neighbor.map in heapentry and neighbor.key < heapentry[neighbor.map][2].key:
                    hindex = heap.index((heapentry[neighbor.map][2].key,
                                         heapentry[neighbor.map][2].move.value,
                                         heapentry[neighbor.map][2]))
                    heap[int(hindex)] = entry
                    heapentry[neighbor.map] = entry
                    heapify(heap)

    def path(self, initstate, finishnode):
        current = finishnode
        moves = list()

        while initstate != current.state:
            if current.move == Direction.UP:
                movement = "up"
            elif current.move == Direction.DOWN:
                movement = "down"
            elif current.move == Direction.LEFT:
                movement = "left"
            else:
                movement = "right"

            moves.insert(0, movement)
            current = current.parent

        return moves


def generatePuzzle(size, all, c):
    """
    The function generates solvable puzzles permutation
    :param size: length of sizes board
    :param all: all elements should shuffle or only some
    :param c: the coefficient how many element placed on final place
    :return: return the solvable puzzle permutation as array length size ** 2
    """
    state = [i + 1 for i in range(size ** 2)]
    state[size ** 2 - 1] = 0

    random.shuffle(state)

    if all:
        f = [i for i in range(0, int(len(state) * c))]
        # f = [1,2,3,4,5,9,13]
        for i in f:
            l = state.index(i)
            state[l], state[i - 1] = state[i - 1], state[l]

    invCount = 0
    for i in range(size * size - 1):
        for j in range(i+1, size * size):
            if state[i] > state[j]:
                invCount += 1

    # find black pos from bottom
    blank = size - (state.index(0) // size + state.index(0) % size)

    if (size + blank + invCount) % 2 != 0:
        return state, True
    else:
        return state, False


def main():
    # param
    size = 4
    c = 0.40

    # generate solvable permutation of puzzle
    initstate = generatePuzzle(size, True, c)
    while not initstate[1]:
        print(initstate)
        initstate = generatePuzzle(size, True, c)

    print(initstate)

    # unplaced puzzle
    # p = Puzzle(size)
    # f = p.astar(initstate[0], "unplaced")
    # pa = p.path(initstate[0], f)
    # print("Długośc scieżki", len(pa), p.nodesExpanded, pa)

    # manhattan
    p2 = Puzzle(size)
    f2 = p2.astar(initstate[0], "manhattan")
    pa2 = p2.path(initstate[0], f2)
    print("Długośc scieżki", len(pa2), p2.nodesExpanded, pa2)


if __name__ == '__main__':
    main()
