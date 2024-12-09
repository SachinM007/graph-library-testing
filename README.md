# Graph Library Testing Project

## Overview
This project implements a comprehensive graph library with various graph algorithms and a robust testing suite.

## Features
- Graph creation and manipulation
- Depth-first and breadth-first traversal
- Cycle detection
- Connectivity checking
- Dijkstra's shortest path algorithm

## Testing Approaches
1. **Pytest Unit Tests**
   - Comprehensive test coverage
   - Tests all library methods
   - Edge case handling

2. **TSTL Test Generation**
   - Automated random test generation
   - Explores various graph operations
   - Helps find unexpected behavior

3. **Mutation Testing**
   - Uses `mutmut` to inject bugs
   - Validates test suite effectiveness
   - Identifies potential weaknesses

## Setup and Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
```bash
# Run unit tests
pytest tests/

# Run coverage
coverage run -m pytest
coverage report

# Run mutation testing
python tests/mutation_testing.py
```

## Project Structure
```
graph-library/
│
├── src/
│   └── graph.py
│
├── tests/
│   ├── __init__.py
│   ├── test_graph.py
│   ├── tstl_test.py
│   └── mutation_testing.py
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── requirements.txt
├── setup.py
├── .gitignore
├── README.md
└── LICENSE
```
