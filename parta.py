from GeneticAlgorithm import GeneticAlgorithm
import matplotlib as mpl
mpl.use('QtAgg')

# parameters
populationSize = 20
chromosomeLength = 30
chanceToMutate = 0.001
generations = 100

gaOnePartOne = GeneticAlgorithm(lambda c: c.count('1'))
ans1_1 = gaOnePartOne.algorithm(populationSize, generations, chanceToMutate)

targetString = GeneticAlgorithm.createGene(chromosomeLength)
gaOnePartTwo = GeneticAlgorithm(lambda c: sum([1 for i in range(len(c)) if c[i] == targetString[i]]))
ans1_2 = gaOnePartTwo.algorithm(populationSize, generations, chanceToMutate)

gaOnePartThree = GeneticAlgorithm(lambda c: 2 * len(c) if c.count('1') == 0 else c.count('1'))
ans1_3 = gaOnePartThree.algorithm(populationSize, generations, chanceToMutate)

def parta():
    mpl.pyplot.plot(ans1_1, 'r')
    mpl.pyplot.plot(ans1_2, 'g')
    mpl.pyplot.plot(ans1_3, 'b')
    mpl.pyplot.xlabel('Generation')
    mpl.pyplot.ylabel('Average Fitness')
    mpl.pyplot.title('Average Fitness of the Population vs Generations')
    mpl.pyplot.show()

if __name__ == "__parta__":
    parta()