import seaborn as sns
import matplotlib.pyplot as plt
from genetic_algorithm import generate_population

sns.set_style("whitegrid")

def lcs(X, Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n]

population = generate_population(10000)
lcs_vec = [lcs(individual[1], ['H','E','L','L','O','W','O','R','L','D']) for individual in population]
gene_dist = sns.distplot(lcs_vec, kde=False, norm_hist=False, color='black', bins=10)
plt.show()