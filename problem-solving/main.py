"""Main Module"""

from problem import Problem
from tree_search import TreeSearch

def main():
    """Main Func"""
    prob = Problem()

    tsearch = TreeSearch()

    result = tsearch.search(prob)

    print(result)



if __name__ == "__main__":
    main()
