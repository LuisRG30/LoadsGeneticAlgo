import random as r

class ValidationError(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

class Individual:
    
    def __init__(self, chromosome=None, alleles=None):
        if chromosome:
            self.chromosome = chromosome
        
        elif not alleles:
            raise ValidationError("Alleles must be indicted when no explicit chromosome is entered.")
        else:
            #Generate random chromosome
            self.chromosome = []
            for i in range(alleles):
                if 0.5 < r.random():
                    self.chromosome.append(0)
                else:
                    self.chromosome.append(1)
                    
    def __str__(self):
        return f"{self.chromosome}"
    
    
    def mutate(self, chance=0.1):
        for i, allele in enumerate(self.chromosome):
            if chance > r.random():
                self.chromosome[i] = 1 - allele
    
    def crossover(self, partner, kind='middle'):
        if len(self.chromosome) == len(partner.chromosome):
            
            if kind == 'middle':
                half = len(self.chromosome) // 2
                chromosome1 = self.chromosome[0:half] + partner.chromosome[half::]
                chromosome2 = partner.chromosome[0:half] + self.chromosome[half::]
                
            elif kind == 'uniform':
                chromosome1 = []
                chromosome2 = []
                for i in range(len(self.chromosome)):
                    if i % 2 == 0:
                        chromosome1.append(self.chromosome[i])
                        chromosome2.append(partner.chromosome[i])
                    else:
                        chromosome2.append(self.chromosome[i])
                        chromosome1.append(partner.chromosome[i])
                        
            elif kind == 'random':
                chromosome1 = []
                chromosome2 = []
                for i in range(len(self.chromosome)):
                    if 0.5 < r.radom():
                        chromosome1.append(self.chromosome[i])
                        chromosome2.append(partner.chromosome[i])
                    else:
                        chromosome2.append(self.chromosome[i])
                        chromosome1.append(partner.chromosome[i])
                        
            else:
                raise ValidationError("Unavailable crossover option selected.")
            
        else:
            raise ValidationError("Chromosome lengths do not match.")
            
        return Individual(chromosome=chromosome1), Individual(chromosome=chromosome2)

