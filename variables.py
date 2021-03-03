import random

#Number of individuals in the network
number_individuals = 1000

#Number of genes and bacteria to simulate and their initial proportion
number_virulence_genes = 100
number_resistance_genes = 100
number_bacteria = 5
min_proportion_virulence_genes = 1/100
max_proportion_virulence_genes = 1/50
min_proportion_resistance_genes = 1/100
max_proportion_resistance_genes = 1/50
min_proportion_bacteria = 1/100
max_proportion_bacteria = 1/50

#Probabilities of transmission upon a contact between two individuals
prob_transmission_bacteria = 0.15
prob_transmission_virulence_genes = 0.01
prob_transmission_resistance_genes = 0.01

#Probability of each of the genes to be eliminated (from 1 to 0) when an antibiotic is administered
prob_antibiotic_eliminate_virulence_genes = 0.7
prob_antibiotic_eliminate_resistance_genes = 0.7

#1 to simulations with no antibiotic, 0 otherwise 
people_no_antibiotic = 0*number_individuals
individuals_no_antibiotic = random.sample(range(0,number_individuals), people_no_antibiotic)

#Total number of antibiotics considered in the simulations 
number_antibiotics = 5

#Number of the neighbors in the network construction
number_neighbors = 4
margin_neighbors = int(number_neighbors/2)

#0 for regular network, 0.5 to small-world network, 1 to random network 
network_type = 0.5

#Loss rate of resistance genes
loss_rate_resistance_genes = 0.005

#Cycles to run
number_cycles = 500

#Number of target genes of each antibiotic
number_target_genes = number_resistance_genes//number_antibiotics




