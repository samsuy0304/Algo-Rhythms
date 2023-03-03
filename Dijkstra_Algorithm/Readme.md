# Dijkstra's Algorithm in Python

This repository contains a Python implementation of Dijkstra's algorithm for finding the shortest path in a weighted graph. The implementation uses a priority queue to efficiently explore the graph and update the distances to each node.

## Requirements

This implementation requires Python 3 and the `heapq` module,

## Usage

The `dijkstra` function in `dijkstra.py` takes a graph represented as a dictionary of dictionaries, where the keys are nodes and the values are dictionaries of neighbors and their corresponding edge weights. Here is an example graph:

```python
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 3, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 6, 'C': 1}
}
```

To find the shortest path from node 'A' to node 'D', you can call the dijkstra function like this:

```python
from dijkstra import dijkstra

distances = dijkstra(graph, 'A', 'D')
print(distances['D']) # prints 5
```


If you omit the end parameter, the function will return a dictionary of distances to all other nodes:

```python
distances = dijkstra(graph, 'A')
print(distances) # prints {'A': 0, 'B': 3, 'C': 4, 'D': 5}
```

# Acknowledgments
This implementation was inspired by the [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) article on Wikipedia.
