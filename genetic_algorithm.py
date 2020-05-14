import random
import argparse

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
target = ['H','E','L','L','O','W','O','R','L','D']

def hamming_distance(ind1, ind2):
	if len(ind1) == len(ind2):
		count = 0
		for i in range(len(ind1)):
			if ind1[i]!=ind2[i]:
				count+=1
		return count

def fitness_score(individual):
	# scale fitness between 0 and 10
	return len(individual) - hamming_distance(individual, target)


def generate_population(size):
	population = []
	for i in range(size):
		individual = []
		for i in range(10):
			individual.append(random.choice(alphabet))
		population.append(individual)
	return list(map(lambda ind: (fitness_score(ind), ind), population))

def select_k_best(genotypes, k):
	genotypes.sort(reverse=True, key=lambda ind: ind[0])
	selected = genotypes[:k]
	suppressed = genotypes[k:]
	return selected, suppressed

def crossover(genotypes, locus=3, n_loci=5):
	children = []
	for i in range(int(len(genotypes)/2)):
		x = genotypes.pop()[1]
		y = genotypes.pop()[1]
		pos = locus * len(x)//n_loci
		children.append(x[:pos]+y[pos:])
		children.append(y[:pos]+x[pos:])
	return list(map(lambda ind: (fitness_score(ind), ind), children))

def snp_mutation(genotypes, rate=0.2):
	for genotype in genotypes:
		if(random.random() < rate):
			genotype[1][random.randint(0,len(genotype[1])-1)] = random.choice(alphabet)
	return list(map(lambda ind: (fitness_score(ind[1]), ind[1]), genotypes))


def evolve(genotypes, select, mut_rate):
	selected_genotypes, suppressed_genotypes = select_k_best(genotypes, k=select)
	print(selected_genotypes[0])
	evolved_genotypes = crossover(selected_genotypes, locus=random.randrange(1,5))
	genotypes = evolved_genotypes + suppressed_genotypes
	genotypes = snp_mutation(genotypes, rate=mut_rate)
	return genotypes


if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-np','--population', type=int, default=10000, help='Size of the initial population.')
	parser.add_argument('-ng','--epochs', type=int, default=25)
	parser.add_argument('-k','--select', type=int, default=400)
	parser.add_argument('-r','--mut_rate', type=float, default=0.2)
	args = parser.parse_args()

	genotypes = generate_population(size=args.population)
	for i in range(args.epochs):
		genotypes = evolve(genotypes, args.select, args.mut_rate)



	
	