import subprocess
import sys
import os

def run_mutation_testing():
    """
    Run mutation testing on the graph library
    
    This script uses mutmut to inject mutations and analyze test effectiveness
    """
    # Ensure we're in the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Change to project root
    os.chdir(project_root)
    
    # Run mutation testing
    try:
        result = subprocess.run([
            'mutmut', 'run', 
            '--paths-to-mutate', 'src/graph.py',
            '--runner', 'pytest tests/'
        ], capture_output=True, text=True)
        
        print("Mutation Testing Results:")
        print(result.stdout)
        
        # Check for any surviving mutations
        if 'survived' in result.stdout:
            print("WARNING: Some mutations survived the test suite!")
        else:
            print("Excellent! All mutations were killed.")
    
    except Exception as e:
        print(f"Error running mutation testing: {e}")

def generate_mutation_report():
    """Generate a detailed mutation testing report"""
    try:
        result = subprocess.run([
            'mutmut', 'results'
        ], capture_output=True, text=True)
        
        with open('mutation_report.txt', 'w') as f:
            f.write(result.stdout)
        
        print("Mutation report saved to mutation_report.txt")
    
    except Exception as e:
        print(f"Error generating mutation report: {e}")

if __name__ == "__main__":
    run_mutation_testing()
    generate_mutation_report()
