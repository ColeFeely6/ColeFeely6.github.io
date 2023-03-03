---
layout: page
title: Connect Four Artificial Intelligence 
description: A program that will optimally play variations of a Connect Four game against you using AI algorithms learned in CS 383
img: assets/img/connect-4-1.webp
importance: 2
category: work
---

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/ai.jpeg" title="ai" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>


<a href="https://github.com/ColeFeely6/Connect-Four-Artificial-Intelligence">GitHub Repository</a>

Connect 4 Artificial Intelligence was a project in my Computer Science Artificial Intelligence class. This project was also a challenge, where every student's program was pinned against each other in a competition. The goal was to create an AI that would optimally play Connect-4 against you. 

Our programs had to be able to play on boards of varying dimensions, from anything like a 4x4 board, a 8x8 board, 6x7, 8x4, 12x8 and so on. 

The program first step was creating a baseline algorithm to find the next move. I used the Minimax Algorithm based on the utility. 

<div class="container">
    <div class="row">
        <div class="col-sm mt-3 mt-md-0">
            {% include figure.html path="assets/img/connnect-four.jpeg" title="connect 4" class="img-fluid rounded z-depth-1" %}
        </div>
    </div>
</div>

Next I used the heuristic evaluation as a baseline, where the heuristic evaluation is invoked when the Minimax algorithm reaches a certain depth limit. This evaluation is considered the "brain" of this Connect-4 bot. The function returns an estimated utility function (either positive or negative) for any game state. 

Finally, I implemented the Alpha-Beta Pruning algorithm, a more efficient and effective AI algorithm. 

The link to the repository is posted above, you can also check it out over on the repository tab on this website!

{% highlight python linenos %}
import random
import math


BOT_NAME = "Cole and Zach's Robot"


## Todo:
# See if **arguments are needed
# Edit evaluation function
# Do prune

class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def __init__(self, stand_dev=None):
        if stand_dev is None:
            self.st = None
        else:
            random.seed(stand_dev)
            self.st = random.getstate()

    def get_move(self, state):
        if self.st is not None:
            random.setstate(self.st)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state):
        """Determine the minimax utility value of the given state.
        Args:
            state: a connect383.GameState object representing the current board
        Returns: the exact minimax utility value of the state
        """
        # #
        # # Fill this in!
        # #
        # return 42  # Change this line!

        nextp = state.next_player()

        if nextp == 1:
            return_value = self.get_max_value(state)

        elif nextp == -1:
            return_value = self.get_min_value(state)

        else:
            return_value = 0

        return return_value

    def get_max_value(self, state):
        return_value = -math.inf
        succs = state.successors()

        if state.is_full() is True:
            return state.utility()

        for i, j in succs:
            maximum = self.get_min_value(j)
            return_value = max(return_value, maximum)

        return return_value

    def get_min_value(self, state):
        return_value = math.inf
        succs = state.successors()


        if state.is_full() is True:
            return state.utility()

        for i, j in succs:
            minimum = self.get_max_value(j)
            return_value = min(return_value, minimum)

        return return_value


class MinimaxHeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move.
    Hint: Consider what you did for MinimaxAgent. What do you need to change to get what you want?
    """

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.
        The depth data member (set in the constructor) determines the maximum depth of the game
        tree that gets explored before estimating the state utilities using the evaluation()
        function.  If depth is 0, no traversal is performed, and minimax returns the results of
        a call to evaluation().  If depth is None, the entire game tree is traversed.
        Args:
            state: a connect383.GameState object representing the current board
        Returns: the minimax utility value of the state
        """
        # #
        # # Fill this in!
        # #
        # return 9  # Change this line!


        nextp = state.next_player()

        if nextp == -1:
            return_value = self.get_min_value(state, depth=0)  # find min value


        elif nextp == 1:
            return_value = self.get_max_value(state, depth=0) # find max value

        else:
            return_value = 0

        return return_value

    def get_max_value(self, state, depth):

        if state.is_full():
            return state.utility()

        if depth >= self.depth_limit:
            return self.evaluation(state)


        return_value = math.inf
        for move, successor in state.successors():
            next = self.get_min_value(successor, depth+1)
            if next < return_value: # get the minimum
                return_value = next
        return return_value

        #return min([self.minimax_depth(successor, depth + 1) for move, successor in state.successors()])

        ## Reviewed by Cole
        # return_value = -math.inf
        # succs = state.successors()
        #
        # if depth >= self.depth_limit:
        #     return self.evaluation(state)
        #
        # if state.is_full():
        #     return state.utility()
        #
        # for i, j in succs:
        #     maximum = self.get_max_value(j, depth=next_depth)
        #     return_value = min(return_value,maximum)
        #
        # return return_value

    def get_min_value(self, state, depth):


        if state.is_full():
            return state.utility()

        if depth >= self.depth_limit:
            return self.evaluation(state)


        return_value = -math.inf
        for move, successor in state.successors():
            next = self.get_max_value(successor, depth + 1)
            if next > return_value:  # get the maximum
                return_value = next
        return return_value



        #
        #
        # ## Reviewed by Cole
        # return_value = math.inf
        # succs = state.successors()
        # curr_depth = arguments["depth"]
        #
        # if curr_depth == self.depth_limit:
        #     return self.evaluation(state)
        #
        # if state.is_full():
        #     return state.utility()
        #
        # next_depth = curr_depth + 1
        #
        # for i, j in succs:
        #     minimum = self.get_min_value(j, depth=next_depth)
        #     return_value = min(return_value, minimum)
        #
        # return return_value

    def minimax_depth(self, state, depth):
        """This is just a helper method fir minimax(). Feel free to use it or not. """

        # return 4 # Change this line!


    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.
        N.B.: This method must run in O(1) time!
        Args:
            state: a connect383.GameState object representing the current board
        Returns: a heuristic estimate of the utility value of the state
        """
        # #
        # # Fill this in!
        # #

        # Change this line!
        # Note: This cannot be "return state.utility() + c", where c is a constant.
        #
        # number_of_columns = state.num_cols
        # ci = number_of_columns // 2
        #
        # stand_dev = math.ceil(number_of_columns / 4)
        # weights = []
        #
        # for i in range(-ci, ci + 1):
        #     w = number_of_columns * (pow(math.pi * 2, -0.5) * pow(stand_dev, -1)) * math.exp(-0.5 * pow((i / stand_dev), 2))
        #     weights.append(w)
        #
        # columns = state.get_cols()
        # h = 0
        # count = 0
        # for column in columns:
        #     h += (column.count(1) - column.count(-1)) * weights[count]
        #     count += 1
        #
        # return h
        #
        weights = []


        number_of_cols = state.num_cols
        ci = number_of_cols // 2

        stand_dev = math.ceil(number_of_cols / 4)


        for i in range(-ci, ci + 1):
            sd1 = pow(math.pi * 2, -0.5) * pow(stand_dev, -1)
            sd2 = math.exp(-0.5 * pow((i / stand_dev), 2))
            weight = number_of_cols * sd1 * sd2
            weights.append(weight)

        columns = state.get_cols()


        return_val = 0
        count = 0
        for col in columns:
            return_val += (col.count(1) - col.count(-1)) * weights[count]
            count += 1

        return return_val

class MinimaxPruneAgent(MinimaxAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move.
    Hint: Consider what you did for MinimaxAgent. What do you need to change to get what you want?
    """

    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.
        The value should be equal to the one determined by MinimaxAgent.minimax(), but the
        algorithm should do less work.  You can check this by inspecting the value of the class
        variable GameState.state_count, which keeps track of how many GameState objects have been
        created over time.  This agent should also respect the depth limit like HeuristicAgent.
        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.
        Args:
            state: a connect383.GameState object representing the current board
        Returns: the minimax utility value of the state
        """
        # #
        # # Fill this in!
        # #
        # return 13  # Change this line!
        nextp = state.next_player()
        if nextp == -1:
            is_max_player = True
            return_value = self.alphabeta(state, -math.inf, math.inf, is_max_player)


        elif nextp == 1:
            is_max_player = False
            return_value = self.alphabeta(state, -math.inf, math.inf, is_max_player)

        else:
            return_value = 0

        return return_value


    def get_min_value(self, state, **kwargs):
        alpha = kwargs["alpha"]
        beta = kwargs["beta"]
        current_depth = kwargs["depth"]

        if current_depth == self.depth_limit:
            return self.evaluation(state)
        if state.is_full():
            return state.utility()

        v = math.inf

        successors = state.successors()
        next_depth = current_depth + 1
        for a, s in successors:
            v = min(v, self.get_max_value(s, alpha=alpha, beta=beta, depth=next_depth))
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v


    def get_max_value(self, state, **kwargs):
        alpha = kwargs["alpha"]
        beta = kwargs["beta"]
        current_depth = kwargs["depth"]

        if state.is_full():
            return state.utility()

        if current_depth == self.depth_limit:
            return self.evaluation(state)

        v = -math.inf

        successors = state.successors()
        next_depth = current_depth + 1
        for a, s in successors:
            v = max(v, self.get_min_value(s, alpha=alpha, beta=beta, depth=next_depth))
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    def alphabeta(self, state, alpha, beta, is_max_player):
        """ This is just a helper method for minimax(). Feel free to use it or not. """
        # return 9 # change this line!

        if state.is_full() == True:
            return state.utility()


        if is_max_player == True:
            best_value = -math.inf
            for move, successor in state.successors():
                best_value = max(best_value, self.alphabeta(successor, alpha, beta, False))
                if best_value >= beta:
                    break
                beta = min(beta, best_value)
            return best_value
        else:
            best_value = math.inf
            for move, successor in state.successors():
                best_value = min(best_value, self.alphabeta(successor, alpha, beta, True))
                if best_value  <= alpha:
                    break
                beta = max(alpha, best_value)
            return best_value







class OtherMinimaxHeuristicAgent(MinimaxAgent):
    """Alternative heursitic agent used for testing."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state."""
        #
        # Fill this in, if it pleases you.
        #
        return 26  # Change this line, unless you have something better to do.

{% endhighlight %}

