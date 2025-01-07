import random
import math
from Fitness import Fitness
from Population import Population
from Optimization import Optimization

class GeneticAlgorithm:
    def __init__(self, file_path,population_size):
        self.population = Population(file_path).initialize_population(population_size)
        self.fitness = Fitness()
        self.optimization = Optimization()
    
    def run(self,epochs,TOURNAMENT_SIZE,MUTATION_RATE,CROSSOVER_RATE,TARGET):
        gen_number = 0
        self.population = self.fitness.calculate_path_distance(self.population)
        plot=[]
        
        for i in range(epochs):
            
            new_population = []
            new_population.append(sorted(self.population)[0][1])
            new_population.append(sorted(self.population)[1][1])
            
            for j in range(int((len(self.population) - 2) / 2)):
                
                if random.random() < CROSSOVER_RATE:
                    offspring1 , offspring2 = self.optimization.selection_crossover(self.population,TOURNAMENT_SIZE)
                else:
                    offspring1 = sorted(random.choices(self.population, k=TOURNAMENT_SIZE))[0][1]
                    offspring2 = sorted(random.choices(self.population, k=TOURNAMENT_SIZE))[0][1]
                offspring1 = self.optimization.mutate(offspring1, MUTATION_RATE)
                offspring2 = self.optimization.mutate(offspring2, MUTATION_RATE)
                new_population.append(offspring1)
                new_population.append(offspring2)
            
            self.population = self.fitness.calculate_path_distance(new_population)
            
            gen_number += 1
            
            if gen_number % 10 == 0:
                print(gen_number, sorted(self.population)[0][0])

            plot.append(sorted(self.population)[0][0])
            if sorted(self.population)[0][0] < TARGET:
                break

        answer = sorted(self.population)[0]

        return answer , plot

if __name__ == "__main__":
    random.seed(13333)

    file_path = r"tsp\berlin52.tsp"
    population_size = 200
    epochs = 100
    TOURNAMENT_SIZE = 10
    MUTATION_RATE = 0.9
    CROSSOVER_RATE = 0.9
    TARGET = 8500

    genetic_algorithm = GeneticAlgorithm(file_path,population_size)
    answer,plot = genetic_algorithm.run(epochs,TOURNAMENT_SIZE,MUTATION_RATE,CROSSOVER_RATE,TARGET)
    print(answer)
