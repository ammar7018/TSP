import math

class Fitness:

    def __init__(self):
        pass
    
    def calculate_distance_city(self,city1,city2):
        return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)
    
    def calculate_path_distance(self,populations):
        population_with_distance = []
        for population in populations:
            total_distance = 0
            for i in range(len(population) - 1):
                total_distance += self.calculate_distance_city(population[i], population[i + 1])

            total_distance += self.calculate_distance_city(population[-1], population[0])
            population_with_distance.append([total_distance, population])
            
        return population_with_distance
    

if __name__ == "__main__":
    
    fitness = Fitness()
    data = [[('24', 835.0, 625.0), ('16', 725.0, 370.0), ('29', 660.0, 180.0), ('50', 595.0, 360.0)]]
    print(fitness.calculate_path_distance(data))