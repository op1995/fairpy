from fairpy.cake.agents import *
from fairpy.cake.allocations import *
from typing import *
import logging

def proportional_division_with_unequal_shares(agents: List[Agent], agents_demands: dict[str,int], allocation: Allocation, start: float, end: float):
    """
       An algorithm for proportional cake division, with unequal shares. Best known complexity! 2(n-1)*celling(log2(D)), where D is the value of the whole cake.
       All agents must value the cake with the same value D, which is the sum of their demands.
       n<D, meaning value of the whole cake must be greater then the number of agents.


       :param agents: the list of all n agents in the original protocol.
       :param agents_demands: dictionary of agents and their demands.
       :param allocation: the current allocation (will be updated during the run).
       :param start: the leftmost end of the cake that should be allocated.
       :param end: the rightmost end of the cake that should be allocated.
       :return: nothing - the allocation is modified in place.


    *Simple example - 2 actors with same demands and value functions
    >>> Alice = PiecewiseConstantAgent([1,1], "Alice")
    >>> Bob = PiecewiseConstantAgent([1,1], "Bob")
    >>> _agents_demands = {"Alice":1, "Bob":1}
    >>> allocations = Allocation([Alice, Bob])
    >>>
    >>> proportional_division_with_unequal_shares([Alice, Bob], _agents_demands, allocations, 0, 1)
    > Alice gets [(0, 0.5)] with value 1
    > Bob gets [(0.5, 1)] with value 1
    <BLANKLINE>

    *the next example the one for each time the player to the left is put there alone. The one with demands 6,3,3.
    *For this doctest I went ahead and complicated it a little more, to make it interesting :) .
    >>> Alice = PiecewiseConstantAgent([6,4,2], "Alice")
    >>> Bob = PiecewiseConstantAgent([4,4,4], "Bob")
    >>> Cat = PiecewiseConstantAgent([1,8,3], "Cat")
    >>> _agents_demands = {"Alice":6, "Bob":3, "Cat":3}
    >>> allocations = Allocation([Alice, Bob, Cat])
    >>>
    >>> proportional_division_with_unequal_shares([Alice, Bob, Cat], _agents_demands, allocations, 0, 1)
    > Alice gets [(0, 0.3)] with value 6
    > Bob gets [(0.53, 1)] with value 5.64
    > Cat gets [(0.3, 0.53)] with value 3
    <BLANKLINE>

    *Example showing "edge case", as suggested - opposite values
    >>> Alice = PiecewiseConstantAgent([1,1,2,2,2,1], "Alice")
    >>> Bob = PiecewiseConstantAgent([2,2,1,1,1,2], "Bob")
    >>> _agents_demands = {"Alice":5, "Bob":4}
    >>> allocations = Allocation([Alice, Bob])
    >>>
    >>> proportional_division_with_unequal_shares([Alice, Bob], _agents_demands, allocations, 0, 1)
    > Alice gets [(0.333, 1)] with value 7
    > Bob gets [(0,0.333)] with value 4
    <BLANKLINE>

    *Example showing bound is tight - each player gets at least his demand
    >>> Alice = PiecewiseConstantAgent([1,1,1,1], "Alice")
    >>> Bob = PiecewiseConstantAgent([1,1,1,1], "Bob")
    >>> Cat = PiecewiseConstantAgent([1,1,1,1], "Cat")
    >>> Dug = PiecewiseConstantAgent([1,1,1,1], "Dug")
    >>> _agents_demands = {"Alice":1, "Bob":1, "Cat":1, "Dug":1}
    >>> allocations = Allocation([Alice, Bob, Cat, Dug])
    >>>
    >>> proportional_division_with_unequal_shares([Alice, Bob, Cat, Dug], _agents_demands, allocations, 0, 1)
    > Alice gets [(0.0, 0.25)] with value 1
    > Bob gets [(0.25,0.5)] with value 1
    > Cat gets [(0.5,0.75)] with value 1
    > Dug gets [(0.75,1)] with value 1
    <BLANKLINE>

    *Example for which the algorithm DOESN'T work - player with deamnd -1, as all deamnds should be positive integers
    >>> Alice = PiecewiseConstantAgent([1,2,0], "Alice")
    >>> Bob = PiecewiseConstantAgent([1,1,1], "Bob")
    >>> Cat = PiecewiseConstantAgent([0.3,0.4,2.3], "Cat")
    >>> _agents_demands = {"Alice":-1, "Bob":1, "Cat":2}
    >>> allocations = Allocation([Alice, Bob, Cat])
    >>>
    >>> proportional_division_with_unequal_shares([Alice, Bob, Cat], _agents_demands, allocations, 0, 1)

    > Alice gets ??? - stuck!
    > Bob gets 0 - see detailed explanation in documentaion (phase b, writing exapmles)
    > Cat gets [(0,1)] with value 3

    """

    return


def proportional_division_with_irrational_demands(agents: List[Agent], agents_demands: dict[str,float], allocation: Allocation, start: float, end: float):
    return
