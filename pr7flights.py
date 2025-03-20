class Graph:
    def __init__(self):
        self.adjMatrix = []  # Adjacency matrix to store the cost of flight paths
        self.cityIndex = {}  # Dictionary to map city name to index in the matrix
        self.cities = []  # List of cities to map indices

    def addFlight(self, city1, city2, cost):
        if city1 not in self.cityIndex:
            self.cityIndex[city1] = len(self.cities)
            self.cities.append(city1)
            # Add a new row and column in the adjacency matrix for the new city
            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append([0] * len(self.cities))

        if city2 not in self.cityIndex:
            self.cityIndex[city2] = len(self.cities)
            self.cities.append(city2)
            # Add a new row and column in the adjacency matrix for the new city
            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append([0] * len(self.cities))

        # Get the indices of the cities
        u = self.cityIndex[city1]
        v = self.cityIndex[city2]
        # Add the flight costs in both directions (assuming undirected graph)
        self.adjMatrix[u][v] = cost
        self.adjMatrix[v][u] = cost

    def displayMatrix(self):
        print("Adjacency Matrix (Flight Costs):")
        print("        ", end="")
        for city in self.cities:
            print(f"{city:10}", end=" ")
        print()

        for i in range(len(self.cities)):
            print(f"{self.cities[i]:<10}", end=" ")
            for j in range(len(self.cities)):
                print(f"{self.adjMatrix[i][j]:<10}", end=" ")
            print()


# Main function
if __name__ == "__main__":
    flightNetwork = Graph()

    # Adding flight paths with costs (you can change the cost as per your data)
    flightNetwork.addFlight("Pune", "Mumbai", 100)
    flightNetwork.addFlight("Pune", "Bangalore", 300)
    flightNetwork.addFlight("Mumbai", "Bangalore", 200)
    flightNetwork.addFlight("Mumbai", "Hyderabad", 150)
    flightNetwork.addFlight("Bangalore", "Hyderabad", 250)
    flightNetwork.addFlight("Ahemadabad", "Pune", 180)
    flightNetwork.addFlight("Ahemadabad", "Mumbai", 160)

    # Display the adjacency matrix
    flightNetwork.displayMatrix()
