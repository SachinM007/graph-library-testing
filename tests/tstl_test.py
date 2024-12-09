from tstl import *
import sys
import os
import random

# Ensure the source directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from graph import Graph

class GraphTest(tst.TestCase):
    def __init__(self):
        super().__init__()
        self.sut = Graph()
        self.pool = {
            'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'current_graph': None
        }

    def setup(self):
        """Reset the graph for each test run"""
        self.sut = Graph()

    def add_node(self):
        """Action to add a random node"""
        node = random.choice(self.pool['nodes'])
        self.sut.add_node(node)
        return True

    def add_edge(self):
        """Action to add a random edge"""
        if len(self.sut.nodes()) < 2:
            self.add_node()
        
        node1 = random.choice(self.sut.nodes())
        node2 = random.choice(self.sut.nodes())
        
        self.sut.add_edge(node1, node2)
        return True

    def remove_node(self):
        """Action to remove a node"""
        if self.sut.nodes():
            node = random.choice(self.sut.nodes())
            self.sut.remove_node(node)
        return True

    def check_connectivity(self):
        """Verify graph connectivity"""
        try:
            self.sut.is_connected()
            return True
        except Exception:
            return False

    def check_cycle_detection(self):
        """Verify cycle detection"""
        try:
            self.sut.detect_cycle()
            return True
        except Exception:
            return False

def explore_graph():
    """Explore graph operations using TSTL"""
    harness = GraphTest()
    for _ in range(100):  # Run 100 iterations of random graph operations
        action = random.choice([
            harness.add_node,
            harness.add_edge,
            harness.remove_node,
            harness.check_connectivity,
            harness.check_cycle_detection
        ])
        action()

if __name__ == "__main__":
    explore_graph()
