import pytest
import sys
import os
import random

# Ensure the source directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from graph import Graph

class TestGraphBasicOperations:
    def setup_method(self):
        """Create a fresh graph for each test method"""
        self.graph = Graph()

    def test_add_node(self):
        """Test adding a single node"""
        self.graph.add_node('A')
        assert 'A' in self.graph.nodes()

    def test_add_multiple_nodes(self):
        """Test adding multiple nodes"""
        nodes = ['A', 'B', 'C']
        for node in nodes:
            self.graph.add_node(node)
        
        for node in nodes:
            assert node in self.graph.nodes()

    def test_remove_node(self):
        """Test removing a node"""
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.remove_node('A')
        
        assert 'A' not in self.graph.nodes()
        assert 'B' in self.graph.nodes()

    def test_add_edge(self):
        """Test adding an edge between nodes"""
        self.graph.add_edge('A', 'B')
        
        assert self.graph.has_edge('A', 'B')
        assert self.graph.has_edge('B', 'A')  # Undirected graph

    def test_remove_edge(self):
        """Test removing an edge"""
        self.graph.add_edge('A', 'B')
        self.graph.remove_edge('A', 'B')
        
        assert not self.graph.has_edge('A', 'B')
        assert not self.graph.has_edge('B', 'A')

    def test_neighbors(self):
        """Test retrieving neighbors of a node"""
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        
        neighbors = self.graph.neighbors('A')
        assert set(neighbors) == {'B', 'C'}

# Additional test classes for other scenarios (Traversals, Connectivity, etc.)
# ... (rest of the previous test file content)
