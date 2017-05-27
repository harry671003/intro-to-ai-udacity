"""Problem Definition"""
from map import RomanianMap

class Problem:
    """Problem"""
    def __init__(self):
        self.__map = RomanianMap()
        self.initial = {
            "name": "Arad",
            "distance": 0

        }

        self.goal = "Sibiu"

    def get_actions(self, state):
        """Get actions for a state"""
        return self.__map.get_neighbours(state["name"])

    def is_goal(self, state):
        """Returns if it's a goal state"""
        return self.goal == state["name"]

    def get_result(self, state, action):
        """Returns the next state when an action is
        applied on current state"""
        state = state
        return action

