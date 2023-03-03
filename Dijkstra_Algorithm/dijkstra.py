import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random

def dijkstra(graph, start, end=None):
    # Initialize distances and visited set
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    
    # Create a priority queue and add the starting node
    pq = [(0, start)]
    
    # Loop until the queue is empty
    while pq:
        # Pop the node with the smallest distance
        distance, node = heapq.heappop(pq)
        
        # Skip if the node has already been visited
        if node in visited:
            continue
        
        # Mark the node as visited
        visited.add(node)
        
        # Check if the destination node has been reached
        if node == end:
            return distances[node]
        
        # Update the distances of the node's neighbors
        for neighbor, weight in graph[node].items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    
    # If an end node was specified, but not reached, there is no path
    if end is not None:
        return float('inf')
    
    # If no end node was specified, return all distances
    return distances
 

##########Graphing

# Create a random graph with 20 nodes
graph = {}
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
for node in nodes:
    neighbors = {}
    for neighbor in random.sample(nodes, random.randint(1, 5)):
        if neighbor != node:
            neighbors[neighbor] = random.randint(1, 10)
    graph[node] = neighbors

# Create a networkx graph object
G = nx.Graph()

# Add nodes to the graph
for node in graph:
    G.add_node(node)

# Add edges to the graph
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

# Calculate the shortest path using Dijkstra's algorithm
distances = dijkstra(graph, 'A')

# Color the nodes based on their distance from the starting node
node_colors = [distances[node] for node in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap='cool', node_size=500)
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_size=15)
plt.axis('off')
plt.show()
print(distances)
