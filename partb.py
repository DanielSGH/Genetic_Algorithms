from GeneticAlgorithm import GeneticAlgorithm
from binpackingGA import binpackingGA
import matplotlib.pyplot as plt

binpackingGApart = binpackingGA()
ans2 = binpackingGApart.algorithm()

def partb():
    plt.plot(ans2, 'y')

    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness of the Population vs Generations')
    plt.show()


if __name__ == "__partb__":
    partb()