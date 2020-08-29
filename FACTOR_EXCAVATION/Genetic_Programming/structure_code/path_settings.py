# Set path
import sys
import os


parent_path = os.path.dirname(__file__)  # structure_code
root_path = os.path.dirname(parent_path)  # Genetic_Programming
sys.path.append(parent_path)
sys.path.append(root_path)