import random as r

from Individual import Individual

class GeneticLoad:
    
    def __init__(self, products, capacity,
                 population_size=10, 
                 generations=100, 
                 mutation_chance=0.1, 
                 selection_method='tournament',
                 crossover_method='middle'):
        
        self.products = products
        self.capacity = capacity
        self.population_size = population_size
        self.generations = generations
        self.mutation_chance = mutation_chance
        self.crossover_method = crossover_method
        
        
        #Generate random starting population
        self.population = []
        alleles = len(self.products)
        for i in range(population_size):
            individual = Individual(alleles=alleles)
            self.population.append(individual)
            
        
        
        #Stores average fitness of each generation
        self.fitness_history = []
        
        #Stores best individual
        self.best = None
        self.best_fitness = float('-inf')
        
        self.best_fitness_history = []
        
        #Keeps track of next generation's population
        self.new = []
        
    def show_population(self):
        for individual in self.population:
            print(individual)
        
    
    #Returns fitness of single individual (Redefinible by user)
    def fitness(self, number):
        
        #Keep this line as it is
        chromosome = self.population[number].chromosome
        score = 0
        load = 0
        
        #Compute fitness score of individual's chromosome
        for i, allele in enumerate(chromosome):
            if allele == 1:
                score += self.products[i].price
                load += self.products[i].volume
                
        if load > self.capacity:
            score = 0
            
        #Add score to fitness record
        return score
                  
    
    
    def selection(self, kind='tournament'):
        #Select randomly
        candidate1 = r.randint(0, len(self.population)-1)
        candidate2 = r.randint(0, len(self.population)-1)
        
        if self.fitness(candidate1) > self.fitness(candidate2):
            selected1 = candidate1
        else:
            selected1 = candidate2
    
        candidate3 = r.randint(0, len(self.population)-1)
        candidate4 = r.randint(0, len(self.population)-1)
        
        #Make sure there is no repetition
        while candidate3 == selected1 or candidate4 == selected1:
            candidate3 = r.randint(0, len(self.population)-1)
            candidate4 = r.randint(0, len(self.population)-1)
            
        if self.fitness(candidate3) > self.fitness(candidate4):
            selected2 = candidate3
        else:
            selected2 = candidate4
            
        return self.population[selected1], self.population[selected2]
        
               
    
    def step(self):
        #Selection
        #print("Selecting")
        parent1, parent2 = self.selection()
        
        #Crossover
        #print("Crossing")
        child1, child2 = parent1.crossover(parent2)
        
        #Mutation
        #print("Mutating")
        child1.mutate()
        child2.mutate()
        
        #print("Adding to new population")
        #Add to new population
        difference = len(self.population) - len(self.new)
       
        if difference == 1:
            self.new.append(child1)
            
        elif difference > 1:
            self.new.append(child1)
            self.new.append(child2)
        
        
        
    def generation(self):
        #Do steps until getting new population
        
        while len(self.new) < len(self.population):
            self.step()
        self.population = self.new
        self.new = []
        
        #Add average fitness to record
        fitness_sum = 0
        
        for i in range(len(self.population)):
            f = self.fitness(i)
            fitness_sum += f
            
            #Check if new best
            if f > self.best_fitness:
                self.best_fitness = f
                self.best = self.population[i]
            
            
        self.fitness_history.append(fitness_sum / self.population_size)
        
        for i in range(len(self.population)):
            best_yet = float('-inf')
            f = self.fitness(i)
            if f > best_yet:
                best_yet = f
        
        if best_yet > self.best_fitness:
            self.best_fitness_history.append(best_yet)
        else:
            self.best_fitness_history.append(self.best_fitness)
        
        
    
    def solve(self):
        for i in range(self.generations - 1):
            self.generation()
            
        

