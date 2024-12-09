class Graph:
    def __init__(self):
        self._graph = {}

    def add_node(self, node):
        """Add a node to the graph if it doesn't exist."""
        if node not in self._graph:
            self._graph[node] = set()

    def remove_node(self, node):
        """Remove a node and all its connections."""
        if node in self._graph:
            del self._graph[node]
            for other_node in self._graph:
                self._graph[other_node].discard(node)

    def add_edge(self, node1, node2):
        """Add an undirected edge between two nodes."""
        self.add_node(node1)
        self.add_node(node2)
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def remove_edge(self, node1, node2):
        """Remove an edge between two nodes."""
        if node1 in self._graph and node2 in self._graph:
            self._graph[node1].discard(node2)
            self._graph[node2].discard(node1)

    def has_edge(self, node1, node2):
        """Check if an edge exists between two nodes."""
        return node1 in self._graph and node2 in self._graph and node2 in self._graph[node1]

    def neighbors(self, node):
        """Return neighbors of a given node."""
        return self._graph.get(node, set())

    def nodes(self):
        """Return all nodes in the graph."""
        return list(self._graph.keys())

    def depth_first_search(self, start_node):
        """Perform depth-first search traversal."""
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_node)
        return result

    def breadth_first_search(self, start_node):
        """Perform breadth-first search traversal."""
        visited = set([start_node])
        queue = [start_node]
        result = [start_node]

        while queue:
            current_node = queue.pop(0)
            for neighbor in self.neighbors(current_node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    result.append(neighbor)

        return result

    def is_connected(self):
        """Check if the graph is fully connected."""
        if not self._graph:
            return True

        start_node = list(self._graph.keys())[0]
        visited = set(self.depth_first_search(start_node))
        return len(visited) == len(self._graph)

    def detect_cycle(self):
        """Detect if the graph contains a cycle."""
        def has_cycle(node, parent, visited):
            visited.add(node)
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    if has_cycle(neighbor, node, visited):
                        return True
                elif neighbor != parent:
                    return True
            return False

        visited = set()
        for node in self.nodes():
            if node not in visited:
                if has_cycle(node, None, visited):
                    return True
        return False

    def dijkstra(self, start_node):
        """Implement Dijkstra's shortest path algorithm."""
        # Note: For simplicity, this assumes non-negative edge weights
        import math
        
        distances = {node: math.inf for node in self.nodes()}
        distances[start_node] = 0
        unvisited = set(self.nodes())

        while unvisited:
            current_node = min(unvisited, key=lambda node: distances[node])
            unvisited.remove(current_node)

            for neighbor in self.neighbors(current_node):
                # Assume edge weight is 1 for simplicity
                tentative_distance = distances[current_node] + 1
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance

        return distances
