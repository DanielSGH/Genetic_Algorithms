import random
import numpy as np
import json

# parameters
populationSize = 20
chromosomeLength = 30
chanceToMutate = 0.001
generations = 100
elistismSize = 3


# Bin packing specific parameters
numBins = 50
numItems = 150
maxBinWeight = 10
maxItemWeight = 5

class binpackingGA:

    def __init__(self):
        self.items = self.generateItems()
        self.highestFitness = np.zeros(numItems)
        self.highestFitnessValue = 0

    def createArray(self):
        return [np.random.randint(0, numBins) for _ in range(numItems)]

    def generatePopulation(self):
        return [self.createArray() for _ in range(populationSize)]

    def generateItems(self):

        with open('initBins.json') as f:
            data = json.load(f)
        bppdata = data['bpp1']
        global numItems
        numItems = bppdata['numItems']
        items = []
        global maxBinWeight
        maxBinWeight = bppdata['capacity']

        for item in bppdata['items']:
            for i in range(item[1]):
                items.append(item[0])

        if len(items) != numItems:
            print('Error: number of items does not match the number of items in the list')

        return items
    
        # Comment out the above and uncomment the below to generate random items
    
        #return [np.random.randint(1, maxItemWeight) for _ in range(numItems)]

    def totalFitness(self, population):
        fitnesses = np.zeros(len(population))
        for i, chromosome in enumerate(population):
            bins = np.zeros(numBins, dtype=int)
            for j, gene in enumerate(chromosome):
                bins[gene] += self.items[j]
            overweight = 0
            for j in range(len(bins)):
                if bins[j] > maxBinWeight:
                    overweight = bins[j] - maxBinWeight
            if overweight > 0:
                fitnesses[i] = -overweight
            else:
                fitnesses[i] += numBins - np.count_nonzero(bins) + 1

            if fitnesses[i] > self.highestFitnessValue:
                self.highestFitnessValue = fitnesses[i]
                self.highestFitness = bins
                print(f'New highest fitness {fitnesses[i]}')
        return fitnesses

    def rouletteWheelSelect(self, population):
        fitnesses = self.totalFitness(population)
        lowestFitness = np.min(fitnesses)
        if lowestFitness < 0:
            fitnesses += abs(lowestFitness)
        if np.sum(fitnesses) == 0:
            return population[np.random.randint(0, len(population))]
        r = random.uniform(0, np.sum(fitnesses))
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
        newChromosome = []
        for i in range(len(chromosome)):
            if random.random() < chanceToMutate:
                offset = np.random.randint(1, numBins)
                newChromosome.append((chromosome[i] + offset) % numBins)
            else:
                newChromosome.append(chromosome[i])
        return newChromosome

    def algorithm(self):
        initialPopulation = self.generatePopulation()
        avgFitnesses = []
        for i in range(generations):
            fitnesses = self.totalFitness(initialPopulation)
            avgFitness = np.mean(fitnesses)
            sumFitness = np.sum(fitnesses)
            avgFitnesses.append(avgFitness)


            print(f'Generation {i + 1}: Average fitness: {avgFitness}, Total fitness: {sumFitness}')

            sortedpop = [x for _, x in sorted(zip(fitnesses, initialPopulation), key=lambda pair: pair[0], reverse=True)]
            generation = sortedpop[:elistismSize]

            while len(generation) < len(initialPopulation):
                parent1 = self.rouletteWheelSelect(initialPopulation)
                parent2 = self.rouletteWheelSelect(initialPopulation)
                child1, child2 = self.onePointCrossover(parent1, parent2)
                generation.append(self.mutate(child1, chanceToMutate))
                generation.append(self.mutate(child2, chanceToMutate))
            initialPopulation = generation

        print(self.items)
        print(self.highestFitnessValue)
        print(self.highestFitness)
        return avgFitnesses