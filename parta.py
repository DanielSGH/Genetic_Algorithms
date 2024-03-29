from GeneticAlgorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

# parameters
populationSize = 10
chromosomeLength = 30
chanceToMutate = 0.01
generations = 100

gaOnePartOne = GeneticAlgorithm(lambda c : c.count('1'))
ans1_1 = gaOnePartOne.algorithm(populationSize, generations, chanceToMutate)

targetString = GeneticAlgorithm.createGene(chromosomeLength)
gaOnePartTwo = GeneticAlgorithm(lambda c : sum([1 for i in range(len(c)) if c[i] == targetString[i]]))
ans1_2 = gaOnePartTwo.algorithm(populationSize, generations, chanceToMutate)

gaOnePartThree = GeneticAlgorithm(lambda c : 2 * len(c) if c.count('1') == 0 else c.count('1'))
ans1_3 = gaOnePartThree.algorithm(populationSize, generations, chanceToMutate)

def main():
    plt.plot(ans1_1, 'r', label='One-Max')
    plt.plot(ans1_2, 'g', label='Target String')
    plt.plot(ans1_3, 'b', label='Deceptive Landscape')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness of the Population vs Generations')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()