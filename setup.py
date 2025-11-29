from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""

    requirement_lst = []   # FIXED: Define the list before using it

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in file:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Error: The file requirements.txt was not found.")
    
    return requirement_lst

print(get_requirements())
setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Koushik Shaganti',
    author_email='shagantikoushik@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)