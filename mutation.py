# Mutation Function
import copy
import random
from crossover import repair_route

def mutation(chromosome, cities, origin, destination):
    """Create two new chromosomes by applying mutations to a chromosome"""
    route1 = copy.deepcopy(chromosome['route'])
    route2 = copy.deepcopy(chromosome['route'])

    # Ensure we only add cities that are not the origin, destination, or already in the route
    possible_cities_to_add = [city for city in cities if city not in chromosome['route']]

    # If chromosome has only 2 cities, create two new chromosomes by adding a city between the origin and destination (position 1):
    if len(chromosome['route']) == 2:
        route1.insert(1, random.choice(possible_cities_to_add))
        route2.insert(1, random.choice(possible_cities_to_add))

    # If chromosome has 3 or more cities, create a new chromosome by removing a city
    elif len(chromosome['route']) >= 3:
        route1.pop(random.randint(1, len(chromosome['route']) - 1))

        # If chromosome has 3 cities, create a new chromosome by adding a city between the origin and destination (position 1):
        if len(chromosome['route']) == 3:
            route2.insert(1, random.choice(possible_cities_to_add))

        # If chromosome has 4 or more cities, create a new chromosome by swapping two cities
        elif len(chromosome['route']) >= 4:
            idx1, idx2 = random.sample(range(1, len(chromosome['route']) - 1), 2)  # Get two distinct indices
            # Perform the swap
            route2[idx1], route2[idx2] = route2[idx2], route2[idx1]

    # Repair routes if necessary
    route1 = repair_route(route1, origin, destination)
    route2 = repair_route(route2, origin, destination)

    # Create offsprings
    mutated_chromosome1 = {"route": route1}
    mutated_chromosome2 = {"route": route2}

    return mutated_chromosome1, mutated_chromosome2