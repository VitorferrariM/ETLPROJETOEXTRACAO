# Initial setup for the project

# Import necessary modules
import os
import sys

# Create necessary directories
def create_project_structure():
    directories = ["data", "scripts", "notebooks", "output", "config"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created or already exists.")

# Initialize the project
def initialize_project():
    print("Initializing project...")
    create_project_structure()
    print("Project initialized successfully!")

if __name__ == "__main__":
    initialize_project()
