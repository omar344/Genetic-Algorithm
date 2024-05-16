from Libraries import * 
def crossover(parent1, parent2, origin, destination):
    """Create two new chromosomes by applying crossover to two parent chromosomes"""
    route1 = copy.deepcopy(parent1['route'])
    route2 = copy.deepcopy(parent2['route'])

    # Proceed to crossover if both parents have more than two cities and if parents are different
    if min(len(route1), len(route2)) > 2 and route1 != route2:
        # If one of the parents has only 3 cities, then add the other parent's cities to the offspring (otherwise we end up with offsprings which are the same as the parents)
        if min(len(route1), len(route2)) == 3:
            # Randomly select a crossover point
            crossover_point = random.randint(1, min(len(route1), len(route2)) - 1)
            # Perform crossover
            offspring1_route = route1 + route2[crossover_point:]
            offspring2_route = route2 + route1[crossover_point:]

        else:
            # Randomly select a crossover point (between 2 and the minimum length of the two routes -2, to maximise odds of having offsprings different from parents)
            crossover_point = random.randint(2, min(len(route1), len(route2)) - 2)

            # Perform crossover
            offspring1_route = route1[:crossover_point] + route2[crossover_point:]
            offspring2_route = route2[:crossover_point] + route1[crossover_point:]

        # Repair the offsprings routes to avoid repeating cities
        offspring1_route = repair_route(offspring1_route, origin, destination)
        offspring2_route = repair_route(offspring2_route, origin, destination)

        # Create offsprings
        offspring1 = {"route": offspring1_route}
        offspring2 = {"route": offspring2_route}

        return offspring1, offspring2

    # If one or both parents have only one leg, return the parents since offsprings would be the same as parents
    else:
        return parent1, parent2


def repair_route(route, origin, destination):
    """Repair a route by ensuring it starts and ends at the origin and destination, respectively, and by removing repeated cities"""
    # Ensure first city is origin and last city is destination and remove intermediate cities if they are origin or destination
    if route[0] != origin:
        route[0] = origin
    if route[-1] != destination:
        route[-1] = destination
    route = [route[0]] + [city for city in route[1:-1] if city != origin and city != destination] + [route[-1]]

    # Remove repeated cities
    seen = set()
    repaired_route = [seen.add(city) or city for city in route if
                      city not in seen]  # adds city to seen if not already there and, in that case, adds city to fixed_route

    return repaired_route