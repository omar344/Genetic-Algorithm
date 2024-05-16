from Libraries import * 

def get_data():
    """Get the data for the problem"""
    # Define the cost matrix
    connections_cost = np.array([
        # LIS   MAD   PAR   BER   AMS   ROM   ZUR   VIE   POR   BCN   TLS   SXB   GNT   BRU   HAM   FRA   MIL
        [np.inf, 10, 30, np.inf, 55, 65, np.inf, 80, 5, 20, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
        # LIS
        [10, np.inf, 10, 15, np.inf, 25, 30, 30, 15, 10, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],  # MAD
        [30, 15, np.inf, 15, 15, 30, 25, 35, np.inf, 25, 10, 20, np.inf, np.inf, np.inf, np.inf, np.inf],  # PAR
        [40, 15, 25, np.inf, 10, 20, 10, 15, np.inf, np.inf, 15, 15, np.inf, np.inf, 20, np.inf, np.inf],  # BER
        [50, 20, 20, 10, np.inf, 35, 25, 30, np.inf, np.inf, np.inf, np.inf, 10, 5, 30, 20, np.inf],  # AMS
        [70, 25, 35, 20, 35, np.inf, 20, 25, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 10],  # ROM
        [75, 30, 25, 15, 25, 20, np.inf, 10, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 20],  # ZUR
        [75, 35, 45, 15, 30, 25, 10, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf],
        # VIE
        [5, 15, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 15, np.inf, np.inf, np.inf, np.inf, np.inf,
         np.inf, np.inf],  # POR
        [20, 10, 25, np.inf, np.inf, np.inf, np.inf, np.inf, 15, np.inf, 15, np.inf, np.inf, np.inf, np.inf, np.inf,
         np.inf],  # BCN
        [np.inf, np.inf, 10, 15, np.inf, np.inf, np.inf, np.inf, np.inf, 15, np.inf, 10, np.inf, np.inf, np.inf, np.inf,
         np.inf],  # TLS
        [np.inf, np.inf, 20, 15, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 10, np.inf, 15, 10, np.inf, np.inf,
         np.inf],  # SXB
        [np.inf, np.inf, np.inf, np.inf, 10, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 15, np.inf, 5, 25, np.inf,
         np.inf],  # GNT
        [np.inf, np.inf, np.inf, np.inf, 5, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 10, 5, np.inf, 20, 15,
         np.inf],  # BRU
        [np.inf, np.inf, np.inf, 20, 30, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 25, 20, np.inf, 10,
         np.inf],  # HAM
        [np.inf, np.inf, np.inf, np.inf, 20, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 15, 10,
         np.inf, 30],  # FRA
        [np.inf, np.inf, np.inf, np.inf, np.inf, 10, 20, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf,
         30, np.inf],  # MIL
    ])

    # Cities
    cities = ['Lisbon', 'Madrid', 'Paris', 'Berlin', 'Amsterdam', 'Rome', 'Zurich', 'Vienna', 'Porto', 'Barcelona',
              'Toulouse', 'Strasbourg', 'Ghent', 'Brussels', 'Hamburg', 'Frankfurt', 'Milan']

    cost_matrix = pd.DataFrame(connections_cost, index=cities, columns=cities)

    # Define the handling costs
    handling_costs = {'Lisbon': 2, 'Madrid': 3, 'Paris': 4, 'Berlin': 5, 'Amsterdam': 5, 'Rome': 4, 'Zurich': 6,
                      'Vienna': 6, 'Porto': 2, 'Barcelona': 3, 'Toulouse': 4, 'Strasbourg': 5, 'Ghent': 5,
                      'Brussels': 4, 'Hamburg': 6, 'Frankfurt': 6, 'Milan': 6}

    print (50*"*")
    for i in enumerate(cities):
        print("City: ", i[1], "Index: ", i[0])
    print (50*"*")
    # Origin
    origin = input("Enter the index of the origin city: ")
    origin = cities[int(origin)]

    # Destination
    destination = input("Enter the index of the destination city: ")
    destination = cities[int(destination)]
    # City coordinates - for visualisation purposes (Optional)
    cities_coords = {
        'Lisbon': {'latitude': 38.722, 'longitude': -9.139},
        'Madrid': {'latitude': 40.416, 'longitude': -3.703},
        'Paris': {'latitude': 48.856, 'longitude': 2.352},
        'Berlin': {'latitude': 52.520, 'longitude': 13.404},
        'Amsterdam': {'latitude': 52.370, 'longitude': 4.895},
        'Rome': {'latitude': 41.902, 'longitude': 12.496},
        'Zurich': {'latitude': 47.376, 'longitude': 8.541},
        'Vienna': {'latitude': 48.208, 'longitude': 16.373},
        'Porto': {'latitude': 41.157, 'longitude': -8.629},
        'Barcelona': {'latitude': 41.385, 'longitude': 2.173},
        'Toulouse': {'latitude': 43.604, 'longitude': 1.444},
        'Strasbourg': {'latitude': 48.583, 'longitude': 7.745},
        'Ghent': {'latitude': 51.054, 'longitude': 3.717},
        'Brussels': {'latitude': 50.850, 'longitude': 4.351},
        'Hamburg': {'latitude': 53.551, 'longitude': 9.993},
        'Frankfurt': {'latitude': 50.110, 'longitude': 8.683},
        'Milan': {'latitude': 45.464, 'longitude': 9.189}
    }

    return cities, origin, destination, handling_costs, cost_matrix, cities_coords
