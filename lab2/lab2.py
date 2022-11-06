import random
import itertools
from collections import namedtuple

OFFSPRING_SIZE = 1000
GENERATIONS = 100
PROBLEM_SIZE = [5, 10, 20, 100, 500, 1000]
TOURNAMENT_SIZE = 10

individual = namedtuple("individual", ["genome", "fitness"])

def problem(N, seed=None):
    """Creates an instance of the problem"""
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def fitness(genome):
	'''Returns a tuple with the # of distinct elements in the genome and a negative sum of sublists' lenghts'''
	return (len(set(itertools.chain(*genome))), -sum(len(l) for l in genome))

def tournament(population, tournament_size=TOURNAMENT_SIZE):
    return max(random.choices(population, k=tournament_size), key=lambda i: i.fitness)

def mutation(genome, lists):
	'''70% probability of adding a gene, 30% of removing'''
	if random.random()>.3 and len(genome)>1:
		random_index = random.randint(0, len(genome)-1)
		genome.pop(random_index)
		return genome
	else: 
		new_element = random.choice(lists)
		genome.append(new_element)
		return genome

def cross_over(g1, g2):
	'''Simple crossover function'''
	cut1 = random.randint(0, len(g1)-1)
	cut2 = random.randint(0, len(g2)-1)
	return g1[:cut1] + g2[cut2:]

def main():
	for N in PROBLEM_SIZE:
		population = list()
		lists = problem(N, seed=42)

		for g in lists:
			l = list()
			l.append(g)
			population.append(individual(l, fitness(l)))

		for g in range(GENERATIONS):
			offspring = list()
			for i in range(OFFSPRING_SIZE):
				if random.random() < .5: #adjust this number to balance mutation/crossover
					w = tournament(population)
					w = mutation(w.genome, lists)
				else:
					w1 = tournament(population)
					w2 = tournament(population)
					w = cross_over(w1.genome, w2.genome)
				f = fitness(w)
				offspring.append(individual(w, f))
			population += offspring
			population = sorted(population, key=lambda i: i.fitness, reverse=True)
		print(f"N={N}, W={-population[0][1][1]}, BLOAT={int((-population[0][1][1]-N)*100/N)}%")


if __name__ == "__main__":
	main()
