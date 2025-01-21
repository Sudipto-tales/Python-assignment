class AntColony:
    def __init__(self, distances, n_ants, n_iterations, decay):
        self.distances = distances
        self.pheromone = [[1 / len(distances) for _ in distances] for _ in distances]
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay

    def run(self):
        shortest_path = None
        shortest_distance = float('inf')
        for _ in range(self.n_iterations):
            for _ in range(self.n_ants):
                path, distance = self.generate_path()
                if distance < shortest_distance:
                    shortest_path = path
                    shortest_distance = distance
            self.update_pheromones(shortest_path, shortest_distance)
        return shortest_path, shortest_distance

    def generate_path(self):
        path = [0]  # Start from city 0
        visited = {0}
        total_distance = 0
        current_city = 0

        while len(path) < len(self.distances):
            next_city = self.select_next_city(current_city, visited)
            path.append(next_city)
            visited.add(next_city)
            total_distance += self.calculate_distance(current_city, next_city)
            current_city = next_city

        path.append(0)  # Return to start
        total_distance += self.calculate_distance(current_city, 0)
        return path, total_distance

    def select_next_city(self, current_city, visited):
        probabilities = []
        total = 0
        for city, dist in enumerate(self.distances[current_city]):
            if city not in visited and dist != float('inf'):
                prob = self.pheromone[current_city][city] / dist
                probabilities.append((city, prob))
                total += prob

        rand = random.uniform(0, total)
        cumulative = 0
        for city, prob in probabilities:
            cumulative += prob
            if rand <= cumulative:
                return city

    def update_pheromones(self, path, distance):
        for i in range(len(path) - 1):
            self.pheromone[path[i]][path[i+1]] += 1 / distance
        for i in range(len(self.pheromone)):
            for j in range(len(self.pheromone[i])):
                self.pheromone[i][j] *= self.decay

    def calculate_distance(self, city1, city2):
        return self.distances[city1][city2]

# Example usage
def main():
    distances = [
        [float('inf'), 10, 15, 20, 25],
        [10, float('inf'), 35, 25, 30],
        [15, 35, float('inf'), 30, 20],
        [20, 25, 30, float('inf'), 15],
        [25, 30, 20, 15, float('inf')]
    ]

    ant_colony = AntColony(distances, n_ants=10, n_iterations=100, decay=0.5)
    shortest_path, shortest_distance = ant_colony.run()
    print("Shortest path:", shortest_path)
    print("Shortest distance:", shortest_distance)

if __name__ == "__main__":
    import random
    main()
