class Graph:
    def __init__(self):
        self.adjacent_list = {}

    def add_vertex(self, vertex):
        self.adjacent_list[vertex] = []

    def add_edges(self, vertex1, vertex2):
        if vertex1 in self.adjacent_list.keys() and vertex2 in self.adjacent_list.keys():
            if vertex2 not in self.adjacent_list[vertex1]:
                self.adjacent_list[vertex1].append(vertex2)
            if vertex1 not in self.adjacent_list[vertex2]:
                self.adjacent_list[vertex2].append(vertex1)

    def remove_edges(self, vertex1, vertex2):
        if vertex1 in self.adjacent_list.keys() and vertex2 in self.adjacent_list.keys():
            self.adjacent_list[vertex1].remove(vertex2)
            self.adjacent_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adjacent_list.keys():
            for edges in self.adjacent_list[vertex]:
                self.adjacent_list[edges].remove(vertex)
            del self.adjacent_list[vertex]

    def print_graph(self):
        for key in self.adjacent_list:
            print(f"{key}, {self.adjacent_list[key]}")

    def clear_graph(self):
        self.adjacent_list.clear()


g = Graph()
g.clear_graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edges("A", "B")
g.add_edges("A", "C")
g.add_edges("B", "C")
g.add_edges("D", "C")
g.add_edges("D", "A")
g.remove_vertex("D")

g.print_graph()
