import os
import sys

# Define project paths
PROJ_TEST_PATH = os.path.dirname(os.path.abspath(__file__))
PROJ_ROOT_PATH = f"{PROJ_TEST_PATH}/../"
# Add src to Python path
sys.path.insert(0, f"{PROJ_ROOT_PATH}")