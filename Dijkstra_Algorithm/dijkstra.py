from matplotlib.backend_bases import GraphicsContextBase
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random

class GraphVisualizer:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = self.generate_random_graph()

    def generate_random_graph(self):
        graph = {}
        for node in self.nodes:
            neighbors = {}
            for neighbor in random.sample(self.nodes, random.randint(1, 5)):
                if neighbor != node:
                    neighbors[neighbor] = random.randint(1, 10)
            graph[node] = neighbors
        return graph

    def dijkstra(self, start, end=None):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()
        pq = [(0, start)]

        while pq:
            distance, node = heapq.heappop(pq)

            if node in visited:
                continue

            visited.add(node)

            if node == end:
                return distances[node]

            for neighbor, weight in self.graph[node].items():
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

        if end is not None:
            return float('inf')

        return distances

    def visualize_graph(self, distances):
        G = nx.Graph()

        for node in self.graph:
            G.add_node(node)

        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                G.add_edge(node, neighbor, weight=weight)

        if isinstance(distances, dict):
            node_colors = [distances[node] for node in G.nodes()]
        else:
            # Handle the case where distances is not a dictionary (e.g., when no path is found)
            node_colors = [0] * len(G.nodes())

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap='cool', node_size=500)
        nx.draw_networkx_edges(G, pos, width=1)
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_size=15)
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    
    Graph = GraphVisualizer(nodes)
    # Perform Dijkstra's algorithm
    start_node = 'A'
    end_node = 'F'
    distances = Graph.dijkstra(start_node, end_node)

    # Check if the destination node was reached
    if isinstance(distances, dict) and distances.get(end_node, float('inf')) == float('inf'):
        print(f"No path from {start_node} to {end_node}")
    else:
        # Visualize the graph
        Graph.visualize_graph(distances)

        # Print the distances
        print(distances)


