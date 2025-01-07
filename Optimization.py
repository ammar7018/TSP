import math
import random
random.seed(13333)

class Optimization:
    def __init__(self):
        pass
        
    def mutate(self,route, mutation_rate):
        if random.random() < mutation_rate:
            idx1, idx2 = random.sample(range(len(route)), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]
        return route
    
    def selection_crossover(self,populations,TOURNAMENT_SIZE):
        
        parent1 = sorted(random.choices(populations, k=TOURNAMENT_SIZE))[0][1]
        parent2 = sorted(random.choices(populations, k=TOURNAMENT_SIZE))[0][1]
        
        size = len(parent1)
        # Step 1: Select crossover range at random
        start, end = sorted(random.sample(range(1, size - 2), 2))  # Avoid the first and last gene (the hive) (Last element of the list is (length - 1). Thus, it is (length - 2) to avoid the last gene)

        # Step 2: Create offspring by exchanging the selected range
        child1 = parent1[:start] + parent2[start:end] + parent1[end:]
        child2 = parent2[:start] + parent1[start:end] + parent2[end:]

        # Step 3: Determine the mapping relationship to legalize offspring
        mapping1 = {parent2[i]: parent1[i] for i in range(start, end)}
        mapping2 = {parent1[i]: parent2[i] for i in range(start, end)}

        # Step 4: Legalize children with the mapping relationship
        for i in list(range(start)) + list(range(end, size)):
            if child1[i] in mapping1:
                while child1[i] in mapping1:
                    child1[i] = mapping1[child1[i]]
            if child2[i] in mapping2:
                while child2[i] in mapping2:
                    child2[i] = mapping2[child2[i]]

        return child1, child2

if __name__ == "__main__":
    optimization = Optimization()
    data = [[29133.756823598167, 
            [('15', 845.0, 680.0), ('23', 480.0, 415.0), ('50', 595.0, 360.0), ('19', 510.0, 875.0), ('34', 700.0, 580.0), ('38', 795.0, 645.0), ('26', 1215.0, 245.0)]],
            [1000.756823598167, 
            [('15', 588.0, 680.0), ('23', 480.0, 220.0), ('50', 595.0, 360.0), ('19', 510.0, 875.0), ('34', 700.0, 580.0), ('38', 795.0, 645.0), ('26', 1215.0, 245.0)]]
            ]
            
    x1,x2= optimization.selection_crossover(data,7)
    print(optimization.mutate(x1,1))