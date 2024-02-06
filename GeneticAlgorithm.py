import random

class GeneticAlgorithm:
    def __init__(self, fitnessFunction):
        self.fitness = fitnessFunction

    @classmethod
    def createGene(self, n):
        return ''.join([random.choice(['0', '1']) for i in range(n)])

    def generatePopulation(self, size, length):
        return [self.createGene(length) for i in range(size)]

    def averageFitness(self, population):
        return self.totalFitness(population) / len(population)

    def totalFitness(self, population):
        return sum([self.fitness(chromosome) for chromosome in population])

    def rouletteWheelSelect(self, population):
        fitnesses = [self.fitness(chromosome) for chromosome in population]
        totalFit = self.totalFitness(population)
        r = random.uniform(0, totalFit)
        upto = 0
        for i in range(len(population)):
            upto += fitnesses[i]
            if upto > r:
                return population[i]
            
    def onePointCrossover(self, c1, c2):
        point = random.randint(0, len(c1))
        newChromosome1 = c1[:point] + c2[point:]
        newChromosome2 = c2[:point] + c1[point:]
        return newChromosome1, newChromosome2

    def mutate(self, chromosome, chanceToMutate):
        newChromosome = ''
        for i in range(len(chromosome)):
            if random.random() < chanceToMutate:
                if chromosome[i] == '1':
                    newChromosome += '0'
                else:
                    newChromosome += '1'
            else:
                newChromosome += chromosome[i]
        return newChromosome

    def algorithm(self, populationSize, generations, chanceToMutate):
        initialPopulation = self.generatePopulation(populationSize, 30)
        generation = []
        avgFitnesses = []
        for i in range(generations):
            avgFitness = self.averageFitness(initialPopulation)
            avgFitnesses.append(avgFitness)
            sumFitness = self.totalFitness(initialPopulation)
            print(f'Generation {i+1}: Average fitness: {avgFitness}, Total fitness: {sumFitness}')

            while len(generation) < len(initialPopulation):
                parent1 = self.rouletteWheelSelect(initialPopulation)
                parent2 = self.rouletteWheelSelect(initialPopulation)
                child1, child2 = self.onePointCrossover(parent1, parent2)
                generation.append(self.mutate(child1, chanceToMutate))
                generation.append(self.mutate(child2, chanceToMutate))
            initialPopulation = generation
            generation = []
        return avgFitnesses