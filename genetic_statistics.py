import argparse
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from genetic_algorithm import generate_population, evolve

sns.set_style("whitegrid")

def fitness_dist(genotypes):
	fitness_vec = [ind[0] for ind in genotypes]
	fitness_dist = sns.distplot(fitness_vec, kde=False, norm_hist=False, color='black', bins=11)
	fitness_dist.set(xticks=[0,1,2,3,4,5,6,7,8,9,10], xlim=(0,10))
	fitness_dist.set_yscale('log')
	plt.show()

def solution_plot(max_fitness, generation, pop_size):
	df = pd.DataFrame(np.c_[max_fitness, generation, pop_size], columns = ['fitness', 'generation', 'size'])
	grid = sns.FacetGrid(df, col="size", hue="size", palette="tab20c", col_wrap=3, height=1.5)
	grid.map(plt.plot, "generation", "fitness", marker=".")
	grid.map(plt.axhline, y=0, ls=":", c=".5")
	grid.set(xlim=(-.5, 20.5), yticks=[1,2,3,4,5,6,7,8,9,10], ylim=(0, 10.5))
	plt.show()

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-np','--size', type=int, default=100000, help='Size of the initial population.')
	parser.add_argument('-ng','--generations', type=int, default=20)
	args = parser.parse_args()

	genotypes = generate_population(args.size)
	for i in range(args.generations):
		genotypes = evolve(genotypes, 25, 0.2)
	fitness_dist(genotypes)


	#max_fitness = []
	#generation = []
	#pop_size = []
	#for i in range(6):
		#if(i==0):
		#	size=1000
		#if(i==1):
		#	size=5000
		#if(i==2):
		#	size=10000
		#if(i==3):
		#	size=100000
		#if(i==4):
		#	size=200000
		#if(i==5):
		#	size=300000
		#genotypes = generate_population(size)
		#for j in range(20):
		#	genotypes = evolve(genotypes, 200, 0.1)
		#	genotypes.sort(reverse=True, key=lambda ind: ind[0])
		#	max_fitness.append(genotypes[0][0])
		#	generation.append(j)
		#	pop_size.append(size)
		#average
		#for k in range (9):
			#for j in range (10):
	#solution_plot(max_fitness, generation, pop_size)