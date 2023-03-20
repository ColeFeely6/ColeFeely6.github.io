---
layout: page
title: AI Tile Puzzle Solver 
description: An AI that takes an unsolved tile puzzle and optimally solves the puzzle 
img: assets/img/tile-puzzle.webp
importance: 4
category: work
---
<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/coding2.png" title="website" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>




## :newspaper: Introduction

<a href="https://github.com/ColeFeely6/Tile-Puzzle-Solver">GitHub Repository</a>

This was another project for my Artificial Intelligence class, where I was tasked with using my understanding of different search strategies and the ramificatinos of using different heurisitcs to solve a modified version of the classic 8 tile puzzle. The puzzle exists on a 3x3 grid with one open 'blank' space. The goal state is where the open tile is on the top left, followed by all the tiles in numerical order. 

The program takes randomly generated puzzles and uses search strategies to optimally solve it. 


## :mag: Search Streategies 

I implemented Uniform-Cost, Greedy best-first and A* search to find the shortest path to the goal. 

The searches are implemented following the heurisitcs, "number of misplced tiles", "Manhattan Distance" and a modified Manhattan distance that takes into account the different transition costs. Each strategy is then compared to how the basic Breadth First Search would solve the puzzle. 

## :computer: Code

{% highlight python linenos %}

from queue import PriorityQueue
import sys
import puzz
import pdqpq

GOAL_STATE = puzz.EightPuzzleBoard("012345678")

def solve_puzzle(start_state, flavor):
    """Perform a search to find a solution to a puzzle.
    
    Args:
        start_state (EightPuzzleBoard): the start state for the search
        flavor (str): tag that indicate which type of search to run.  Can be one of the following:
            'bfs' - breadth-first search
            'ucost' - uniform-cost search
            'greedy-h1' - Greedy best-first search using a misplaced tile count heuristic
            'greedy-h2' - Greedy best-first search using a Manhattan distance heuristic
            'greedy-h3' - Greedy best-first search using a weighted Manhattan distance heuristic
            'astar-h1' - A* search using a misplaced tile count heuristic
            'astar-h2' - A* search using a Manhattan distance heuristic
            'astar-h3' - A* search using a weighted Manhattan distance heuristic
    
    Returns: 
        A dictionary containing describing the search performed, containing the following entries:
        'path' - list of 2-tuples representing the path from the start to the goal state (both 
            included).  Each entry is a (str, EightPuzzleBoard) pair indicating the move and 
            resulting successor state for each action.  Omitted if the search fails.
        'path_cost' - the total cost of the path, taking into account the costs associated with 
            each state transition.  Omitted if the search fails.
        'frontier_count' - the number of unique states added to the search frontier at any point 
            during the search.
        'expanded_count' - the number of unique states removed from the frontier and expanded 
            (successors generated)

    """

    if flavor.find('-') > -1:
        strat, heur = flavor.split('-')
    else:
        strat, heur = flavor, None

    if strat == 'bfs':
        return BreadthFirstSolver(GOAL_STATE).solve(start_state)

    elif strat == 'ucost':
        return UniformCostSolver(GOAL_STATE).solve(start_state)

    elif strat == 'greedy':
        return GreedySolver(GOAL_STATE).solve(start_state)

    elif strat == 'astar':
        return AStarSolver(GOAL_STATE, heur).solve(start_state)
    # elif strat == 'astar-h1':
    #     return AStarSolver(GOAL_STATE).solve(start_state,'h1')
    #
    # elif strat == 'astar-h2':
    #     return AStarSolver(GOAL_STATE).solve(start_state,'h2')
    #
    # elif strat == 'astar-h3':
    #     return AStarSolver(GOAL_STATE).solve(start_state,'h3')
    else:
        raise ValueError("Unknown search flavor '{}'".format(flavor))


def get_test_puzzles():
    """Return sample start states for testing the search strategies.
    
    Returns:
        A tuple containing three EightPuzzleBoard objects representing start states that have an
        optimal solution path length of 3-5, 10-15, and >=25 respectively.
    
    """
    #
    # fill in function body here
    #
    move_in_three = puzz.EightPuzzleBoard("312459678")
    move_in_ten = puzz.EightPuzzleBoard("320518467")
    move_in_twenty_five = puzz.EightPuzzleBoard("876021534")

    return move_in_three, move_in_ten, move_in_twenty_five  # fix this line!


def print_table(flav__results, include_path=False):
    """Print out a comparison of search strategy results.

    Args:
        flav__results (dictionary): a dictionary mapping search flavor tags result statistics. See
            solve_puzzle() for detail.
        include_path (bool): indicates whether to include the actual solution paths in the table

    """
    result_tups = sorted(flav__results.items())
    c = len(result_tups)
    na = "{:>12}".format("n/a")
    rows = [  # abandon all hope ye who try to modify the table formatting code...
        "flavor  " + "".join(["{:>12}".format(tag) for tag, _ in result_tups]),
        "--------" + ("  " + "-" * 10) * c,
        "length  " + "".join(["{:>12}".format(len(res['path'])) if 'path' in res else na
                              for _, res in result_tups]),
        "cost    " + "".join(["{:>12,}".format(res['path_cost']) if 'path_cost' in res else na
                              for _, res in result_tups]),
        "frontier" + ("{:>12,}" * c).format(*[res['frontier_count'] for _, res in result_tups]),
        "expanded" + ("{:>12,}" * c).format(*[res['expanded_count'] for _, res in result_tups])
    ]

    if include_path:
        rows.append("path")
        longest_path = max([len(res['path']) for _, res in result_tups if 'path' in res])
        print("longest", longest_path)
        for i in range(longest_path):
            row = "        "
            for _, res in result_tups:
                if len(res.get('path', [])) > i:
                    move, state = res['path'][i]
                    row += " " + move[0] + " " + str(state)
                else:
                    row += " " * 12
            rows.append(row)
    print("\n" + "\n".join(rows), "\n")


class PuzzleSolver:
    """Base class for 8-puzzle solver."""

    def __init__(self, goal_state):
        self.parents = {}  # state -> parent_state
        self.expanded_count = 0
        self.frontier_count = 0
        self.goal = goal_state

    def get_path(self, state):
        """Return the solution path from the start state of the search to a target.
        
        Results are obtained by retracing the path backwards through the parent tree to the start
        state for the search at the root.
        
        Args:
            state (EightPuzzleBoard): target state in the search tree
        
        Returns:
            A list of EightPuzzleBoard objects representing the path from the start state to the
            target state

        """
        path = []
        while state is not None:
            path.append(state)
            state = self.parents[state]
        path.reverse()
        return path

    def get_cost(self, state):
        """Calculate the path cost from start state to a target state.
        
        Transition costs between states are equal to the square of the number on the tile that 
        was moved. 

        Args:
            state (EightPuzzleBoard): target state in the search tree
        
        Returns:
            Integer indicating the cost of the solution path

        """
        cost = 0
        path = self.get_path(state)
        for i in range(1, len(path)):
            x, y = path[i - 1].find(None)  # the most recently moved tile leaves the blank behind
            tile = path[i].get_tile(x, y)
            cost += int(tile) ** 2
        return cost

    def get_results_dict(self, state):
        """Construct the output dictionary for solve_puzzle()
        
        Args:
            state (EightPuzzleBoard): final state in the search tree
        
        Returns:
            A dictionary describing the search performed (see solve_puzzle())

        """
        results = {}
        results['frontier_count'] = self.frontier_count
        results['expanded_count'] = self.expanded_count
        if state:
            results['path_cost'] = self.get_cost(state)
            path = self.get_path(state)
            moves = ['start'] + [path[i - 1].get_move(path[i]) for i in range(1, len(path))]
            results['path'] = list(zip(moves, path))
        return results

    def solve(self, start_state):
        # TODO: May need to put stuff in here
        """Carry out the search for a solution path to the goal state.
        
        Args:
            start_state (EightPuzzleBoard): start state for the search 
        
        Returns:
            A dictionary describing the search from the start state to the goal state.

        """
        raise NotImplementedError('Classed inheriting from PuzzleSolver must implement solve()')


class BreadthFirstSolver(PuzzleSolver):
    """Implementation of Breadth-First Search based on PuzzleSolver"""

    def __init__(self, goal_state):
        self.frontier = pdqpq.FifoQueue()
        self.explored = set()
        super().__init__(goal_state)

    def add_to_frontier(self, node):
        """Add state to frontier and increase the frontier count."""
        self.frontier.add(node)
        self.frontier_count += 1

    def expand_node(self, node):
        """Get the next state from the frontier and increase the expanded count."""
        self.explored.add(node)
        self.expanded_count += 1
        return node.successors()

    def solve(self, start_state):
        self.parents[start_state] = None
        self.add_to_frontier(start_state)

        if start_state == self.goal:  # edge case        
            return self.get_results_dict(start_state)

        while not self.frontier.is_empty():
            node = self.frontier.pop()  # get the next node in the frontier queue
            succs = self.expand_node(node)

            for move, succ in succs.items():
                if (succ not in self.frontier) and (succ not in self.explored):
                    self.parents[succ] = node

                    # BFS checks for goal state _before_ adding to frontier
                    if succ == self.goal:
                        return self.get_results_dict(succ)
                    else:
                        self.add_to_frontier(succ)

        # if we get here, the search failed
        return self.get_results_dict(None)


class UniformCostSolver(PuzzleSolver):
    """Implementation of Uniform-Cost Search based on PuzzleSolver"""

    def __init__(self, goal_state):
        self.frontier = pdqpq.PriorityQueue()
        self.explored = set()  # set function creates a set object and are in random order
        # key: child, value: (parent, direction of move, cost up to child)
        # self.tracker = {start_state: (None,"start", 0)}
        super().__init__(goal_state)

    ##TODO/ MAJOR WE NEED TO MODIFY EXPAND NODE SO THAT IT ORDERS THEM BY LOWEST COST
    def add_to_frontier(self, node, cost):
        """Add state to frontier and increase the frontier count."""
        # Frontier is an instance of Priority Queue
        self.frontier.add(node, priority = cost)
        self.frontier_count += 1

    def expand_node(self, node):
        """Get the next state from the frontier and increase the expanded count."""

        self.explored.add(node)
        self.expanded_count += 1
        return node.successors()

    # Need to account for the weights and cost in UCS
    def solve(self, start_state):
        self.parents[start_state] = None
        self.add_to_frontier(start_state, 0)


        if start_state == self.goal:  # edge case        
            return self.get_results_dict(start_state)

        while not self.frontier.is_empty():
            node = self.frontier.pop()  # get the next node in the frontier queue

            if node == self.goal:
                return self.get_results_dict(node)
            succs = self.expand_node(node)


            for move, succ in succs.items():
                if (succ not in self.frontier) and (succ not in self.explored):
                    self.parents[succ] = node

                    # UCS checks for goal state _before_ adding to frontier
                    if succ == self.goal:
                        return self.get_results_dict(succ)
                    else:
                        self.add_to_frontier(succ, self.get_cost(succ))

                elif succ in self.frontier:
                    prev_node = self.parents[succ]
                    prev_cost = self.get_cost(prev_node)
                    new_cost = prev_cost + self.get_cost(succ)
                    self.parents[succ] = succ
                    if self.frontier.get(succ) > new_cost:
                        #need to update, possibly may need to remove then add???
                        self.add_to_frontier(succ, self.get_cost(succ))
                    else:
                        self.parents[succ] = prev_node


        # if we get here, the search failed
        return self.get_results_dict(None)


class GreedySolver(PuzzleSolver):
    """Implementation of Greedy-First Search based on PuzzleSolver"""

    def __init__(self, goal_state):
        self.frontier = pdqpq.FifoQueue()
        self.explored = set()
        super().__init__(goal_state)

    def add_to_frontier(self, node):
        """Add state to frontier and increase the frontier count."""
        self.frontier.add(node)
        self.frontier_count += 1

    def expand_node(self, node):
        """Get the next state from the frontier and increase the expanded count."""
        self.explored.add(node)
        self.expanded_count += 1
        return node.successors()

    def solve(self, start_state):
        self.parents[start_state] = None
        self.add_to_frontier(start_state)

        if start_state == self.goal:  # edge case
            return self.get_results_dict(start_state)

        while not self.frontier.is_empty():
            node = self.frontier.pop()  # get the next node in the frontier queue
            succs = self.expand_node(node)

            for move, succ in succs.items():
                if (succ not in self.frontier) and (succ not in self.explored):
                    self.parents[succ] = node

                    # BFS checks for goal state _before_ adding to frontier
                    if succ == self.goal:
                        return self.get_results_dict(succ)
                    else:
                        self.add_to_frontier(succ)

        # if we get here, the search failed
        return self.get_results_dict(None)


class AStarSolver(PuzzleSolver):
    """Implementation of A* Search based on PuzzleSolver"""


    # AStar will be exactly like UCost, but the cost will also account for the heuristic for the priority queue.
    # The heuristic will depend on what the algorithm passes through

    def __init__(self, goal_state, heur):
        self.frontier = pdqpq.PriorityQueue()
        self.explored = set()  # set function creates a set object and are in random order
        self.heur = heur
        super().__init__(goal_state)


    def add_to_frontier(self, node, cost):
        """Add state to frontier and increase the frontier count."""
        # Frontier is an instance of Priority Queue
        self.frontier.add(node, priority = cost)
        self.frontier_count += 1

    def expand_node(self, node):
        """Get the next state from the frontier and increase the expanded count."""

        self.explored.add(node)
        self.expanded_count += 1
        return node.successors()


    def get_h_cost(self, state):
        if self.heur == 'h1':
            cost = 0
            str_puzz = str(state)
            for i in range(1, 9):
                if i != int(str_puzz[i]):
                    cost += 1
            return cost
        elif self.heur == 'h2':
            cost = 0
            for i in range(1, 9):
                x, y = state.find(str(i))
                x0, y0 = GOAL_STATE.find(str(i))
                cost += abs(x - x0) + abs(y - y0)
            return cost
        elif self.heur == 'h3':
            cost = 0
            for i in range(0, 9):
                x, y = state.find(str(i))
                x0, y0 = GOAL_STATE.find(str(i))
                score = abs(x - x0) + abs(y - y0)
                cost += score * i ** 2
            return cost



    # Need to account for the weights and cost in UCS
    def solve(self, start_state):
        self.parents[start_state] = None
        self.add_to_frontier(start_state, 0)


        if start_state == self.goal:  # edge case
            return self.get_results_dict(start_state)

        while not self.frontier.is_empty():
            node = self.frontier.pop()  # get the next node in the frontier queue

            if node == self.goal:
                return self.get_results_dict(node)
            succs = self.expand_node(node)


            for move, succ in succs.items():
                if (succ not in self.frontier) and (succ not in self.explored):
                    self.parents[succ] = node

                    # UCS checks for goal state _before_ adding to frontier
                    if succ == self.goal:
                        return self.get_results_dict(succ)
                    else:
                        self.add_to_frontier(succ, self.get_cost(succ))

                elif succ in self.frontier:
                    prev_node = self.parents[succ]
                    prev_cost = self.get_cost(prev_node)
                    # Get the h_cost
                    h_cost = self.get_h_cost(succ)
                    new_cost = prev_cost + self.get_cost(succ) + h_cost
                    self.parents[succ] = succ
                    if self.frontier.get(succ) > new_cost:
                        #need to update, possibly may need to remove then add???
                        self.add_to_frontier(succ, self.get_cost(succ))
                    else:
                        self.parents[succ] = prev_node


        # if we get here, the search failed
        return self.get_results_dict(None)

        ############################################


if __name__ == '__main__':

    # parse the command line args
    start = puzz.EightPuzzleBoard(sys.argv[1])
    if sys.argv[2] == 'all':
        flavors = ['bfs', 'ucost', 'greedy-h1', 'greedy-h2',
                   'greedy-h3', 'astar-h1', 'astar-h2', 'astar-h3']
    else:
        flavors = sys.argv[2:]

    # run the search(es)
    results = {}
    for flav in flavors:
        print("solving puzzle {} with {}".format(start, flav))
        results[flav] = solve_puzzle(start, flav)

    print_table(results, include_path=False)  # change to True to see the paths!


{% endhighlight %}

