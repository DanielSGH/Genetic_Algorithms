from GeneticAlgorithm import GeneticAlgorithm
from binpackingGA import binpackingGA
import matplotlib.pyplot as plt

binpackingGApart = binpackingGA()
ans2 = binpackingGApart.algorithm()

plt.plot(ans2, 'y')

plt.xlabel('Generation')
plt.ylabel('Average Fitness')
plt.title('Average Fitness of the Population vs Generations')
fig = plt.gcf()
plt.show()
plt.draw()
fig.savefig('fitness.png', dpi=100)