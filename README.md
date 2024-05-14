# Genetic Algorithm

The shortest path problem involves finding the most efficient route between two points in a network, typically represented as a graph where cities are nodes and roads are edges with associated distances. The goal is to minimize the total distance or time required to travel from a source city to a destination city. This problem finds applications in various fields such as transportation, logistics, and telecommunications.

In this project, we tackle the shortest path problem using a Genetic Algorithm (GA). GAs are optimization techniques inspired by natural selection processes. By iteratively evolving a population of potential solutions, GAs aim to find an approximate shortest path between two cities on a map. This method allows for efficient exploration of solution space and scalability for handling large networks.


# Implementation
## The Genetic Algorithm (GA) is a metaheuristic optimization technique inspired by the process of natural selection and evolution. In the context of solving the shortest path problem between two cities, the GA operates as follows:

1) **Chromosome Representation**: Each chromosome represents a potential solution, which in this case is a sequence of cities representing a path from the source to the destination.

2) **Initialization**: A population of chromosomes is randomly generated to start the optimization process.

3) **Fitness Function**: A fitness function evaluates the quality of each chromosome by calculating the total distance of the path it represents. Shorter paths receive higher fitness scores.

4) **Selection**: Parents for the next generation are selected based on their fitness scores. Common selection methods include roulette wheel selection or tournament selection.

5) **Crossover**: Pairs of parents are combined to produce offspring (new solutions) using techniques like one-point crossover or uniform crossover. This allows for exploration of new paths by combining characteristics of parent solutions.

6) **Mutation**: Random alterations are made to certain genes (cities) in the offspring to introduce diversity into the population and prevent premature convergence to suboptimal solutions.

7) **Survivor Selection**: The offspring and sometimes the parents are evaluated, and a subset is chosen to survive and form the next generation. This selection is typically based on a combination of fitness and diversity criteria.

8) **Termination Condition**: The algorithm continues iterating through generations until a termination condition is met, such as reaching a maximum number of generations or finding a satisfactory solution.






# Installation
create new file **bash.sh** and copy this content inside this file and run it

```bash
#!/bin/bash

# Clone the repository
git clone https://github.com/mo7amedgom3a/Genetic-Algorithm.git

# Navigate to the cloned directory
cd Genetic-Algorithm

python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "Setup completed. Virtual environment activated and dependencies installed."

```

# Example
![Shortest Path GIF](https://github.com/mo7amedgom3a/Genetic-Algorithm/blob/main/_Porto_Zurich.gif?raw=true)


To illustrate the Genetic Algorithm (GA) for finding the shortest path between Porto and Zurich:

1. **Graph Representation**: Consider a simplified map where cities are nodes and connections between cities are edges with associated distances.

2. **Initialization**: Start with a random population of potential solutions (chromosomes), where each chromosome represents a path from Porto to Zurich.

3. **Fitness Evaluation**: Evaluate each chromosome's fitness based on the total distance of the path it represents.

4. **Selection**: Select parents for the next generation based on their fitness scores.

5. **Crossover**: Combine pairs of parents to produce offspring using techniques like one-point crossover or uniform crossover.

6. **Mutation**: Introduce random alterations to certain genes (cities) in the offspring to introduce diversity.

7. **Survivor Selection**: Choose a subset of offspring and sometimes parents to survive and form the next generation.

8. **Termination Condition**: Iterate through generations until reaching a termination condition, such as finding the shortest path or reaching a maximum number of generations.

By applying these steps iteratively, the GA progressively evolves the population towards finding an optimal or near-optimal solution for the shortest path between Porto and Zurich.

# Contributing

Contributions to this project are welcome! The following members have contributed to the development of this project:

- [Mohamed Gomaa](https://github.com/mo7amedgom3a)
- [Omar Abadi](https://github.com/omar344)
- [Ahmed Essam](https://github.com/bad-maths)
- [Adel Awad Al Kazzaz](https://github.com/Adelkazzaz)

If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
