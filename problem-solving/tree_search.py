"""Tree Search Algorithm"""

class TreeSearch:
    """Tree Search Class"""
    def __init__(self):
        """Ctor"""
        self.__frontier = None

    def search(self, problem):
        """Searches given a problem"""
        self.__frontier = [[problem.initial]] # The list of all leaves not observed

        while 1:
            if len(self.__frontier) == 0:
                return False

            path = self.__remove_choice()

            state = path[-1]

            if problem.is_goal(state):
                return path

            for action in problem.get_actions(state):
                result = problem.get_result(state, action)

                new_path = list(path)
                new_path.append(result)
                self.__frontier.append(new_path)

    def __remove_choice(self):
        return self.__frontier.pop()
