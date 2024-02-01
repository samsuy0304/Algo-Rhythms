# Graph Visualizer with Dijkstra's Algorithm

This project implements a graph visualizer using NetworkX and Matplotlib, incorporating Dijkstra's algorithm to find the shortest path between two nodes in a randomly generated graph.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Introduction

This Python project showcases the implementation of a graph visualizer with Dijkstra's algorithm. It uses the NetworkX library for graph representation and Matplotlib for visualization.

## Features

- Random graph generation with customizable nodes and edge weights.
- Dijkstra's algorithm for finding the shortest path between two nodes.
- Visualization of the graph with node colors indicating distances.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/graph-visualizer.git

## Usage

Open the `dijkstra.py` file in your preferred Python environment.

Customize the nodes list to define the nodes in your graph.

Run the script:
`python3 dikjkshit.py`

## Example
```
# Define nodes for the graph
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Create an instance of the GraphVisualizer class
graph_visualizer = GraphVisualizer(nodes)

# Perform Dijkstra's algorithm
start_node = 'A'
end_node = 'F'
distances = graph_visualizer.dijkstra(start_node, end_node)

# Check if the destination node was reached
if isinstance(distances, dict) and distances.get(end_node, float('inf')) == float('inf'):
    print(f"No path from {start_node} to {end_node}")
else:
    # Visualize the graph
    graph_visualizer.visualize_graph(distances)

    # Print the distances
    print(distances)
```
