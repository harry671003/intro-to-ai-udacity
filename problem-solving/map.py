"""Map Module"""

class RomanianMap:
    """The Map of Romania"""

    def __init__(self):
        self.__init_cities()
        self.__init_cities_to_index()
        self.__init_graph()
        self.__init_paths()

    def __init_graph(self):
        self.__graph = [[-1 for i in range(len(self.__cities))] for j in range(len(self.__cities))]

    def __init_cities(self):
        self.__cities = [
            "Arad",
            "Zerind",
            "Oradea",
            "Timisoara",
            "Sibiu",
            "Lugoj",
            "Mehadia",
            "Drobeta",
            "Fagaras",
            "Rimnicu Vilcea",
            "Craiova",
            "Pitesti",
            "Bucharest",
            "Giurgiu",
            "Urziceni",
            "Hirsova",
            "Eforie",
            "Vaslui",
            "Iasi",
            "Neamt"
        ]

    def __init_cities_to_index(self):
        self.__city_index = {}

        for index, city in enumerate(self.__cities):
            self.__city_index[city] = index

    def __init_paths(self):
        self.__create_path("Arad", "Zerind", 75)
        self.__create_path("Arad", "Timisoara", 118)
        self.__create_path("Zerind", "Oradea", 71)
        self.__create_path("Arad", "Sibiu", 140)
        self.__create_path("Oradea", "Sibiu", 151)
        self.__create_path("Timisoara", "Lugoj", 111)
        self.__create_path("Lugoj", "Mehadia", 70)
        self.__create_path("Mehadia", "Drobeta", 75)
        self.__create_path("Drobeta", "Craiova", 120)
        self.__create_path("Sibiu", "Rimnicu Vilcea", 80)
        self.__create_path("Rimnicu Vilcea", "Craiova", 146)
        self.__create_path("Rimnicu Vilcea", "Pitesti", 97)
        self.__create_path("Craiova", "Pitesti", 138)
        self.__create_path("Sibiu", "Fagaras", 99)
        self.__create_path("Fagaras", "Bucharest", 211)
        self.__create_path("Pitesti", "Bucharest", 101)
        self.__create_path("Bucharest", "Giurgiu", 90)
        self.__create_path("Bucharest", "Urziceni", 85)
        self.__create_path("Urziceni", "Vaslui", 142)
        self.__create_path("Urziceni", "Hirsova", 98)
        self.__create_path("Vaslui", "Iasi", 92)
        self.__create_path("Iasi", "Neamt", 87)
        self.__create_path("Hirsova", "Eforie", 86)



    def __create_path(self, city_a, city_b, distance):
        city_a_index = self.__city_index[city_a]
        city_b_index = self.__city_index[city_b]

        self.__graph[city_a_index][city_b_index] = distance
        self.__graph[city_b_index][city_a_index] = distance

    def __str__(self):
        return str(self.__graph)

    def get_neighbours(self, city):
        """Get the neighbours for a current city"""
        current_city_index = self.__city_index[city]
        neighbours = []

        for city_index, cost in enumerate(self.__graph[current_city_index]):
            if cost > -1:
                neighbours.append({
                    "name": self.__cities[city_index],
                    "cost": cost
                })

        return neighbours

