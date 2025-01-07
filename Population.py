import math
import random
random.seed(13333)

class Population:
    def __init__(self,file_path):
        self.cities = []
        with open(file_path, 'r') as file:
            for line in file: 
                try:
                    num, x, y = line.split()  
                    self.cities.append((num.strip(), float(x), float(y)))  
                except:  # If there's an error (e.g., invalid line format), skip this line
                    continue
        
    def initialize_population(self,population_size):
        if population_size > math.factorial(len(self.cities)):
            raise ValueError("Population size exceeds the total number of unique permutations.")
        
        population = set()
        while len(population) < population_size:
            route = tuple(random.sample(self.cities, len(self.cities)))
            population.add(route)
        return [list(route) for route in population]

if __name__ == "__main__":
    population = Population(r"tsp\berlin52.tsp")
    print(population.initialize_population(2000))