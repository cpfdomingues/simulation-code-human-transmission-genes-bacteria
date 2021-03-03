import variables
import random

def virulence_genes():

    """
    Returns a list of lists, each list having the virulence genes of an individual
    """

    virulence_genes_data = []

    for each_individual in range(1, variables.number_individuals + 1):
        list_to_add = variables.number_virulence_genes*[0]
        virulence_genes_data.append(list_to_add)
    for each_virulence_gene in range(0, variables.number_virulence_genes):
        number_times_virulence_gene_exists = random.sample(range(int(variables.min_proportion_virulence_genes*variables.number_individuals), int(variables.max_proportion_virulence_genes*variables.number_individuals)), 1)
        individuals_with_virulence_gene = random.sample(range(0, variables.number_individuals), number_times_virulence_gene_exists[0]) 
        for each_individual in individuals_with_virulence_gene:
            virulence_genes_data[each_individual][each_virulence_gene] = 1
            
    return (virulence_genes_data)


def resistance_genes():

    """
    Returns a list of lists, each list having the resistance genes of an individual
    """
    
    resistance_genes_data = []
    
    for each_individual in range(1, variables.number_individuals + 1):
        list_to_add = variables.number_resistance_genes*[0]
        resistance_genes_data.append(list_to_add)
    for each_resistance_gene in range(0, variables.number_resistance_genes):
        number_times_resistance_gene_exists = random.sample(range(int(variables.min_proportion_resistance_genes*variables.number_individuals), int(variables.max_proportion_resistance_genes*variables.number_individuals)), 1)
        individuals_with_resistance_gene = random.sample(range(0, variables.number_individuals), number_times_resistance_gene_exists[0])
        for each_individual in individuals_with_resistance_gene:
            resistance_genes_data[each_individual][each_resistance_gene] = 1

    return (resistance_genes_data)


def bacteria():

    """
    Returns a list of lists, each list having the bacteria of an individual
    """

    bacteria_data = []
    for each_individual in range(1, variables.number_individuals + 1):
        list_to_add = variables.number_bacteria*[0]
        bacteria_data.append(list_to_add)
    for each_bacterium in range(0, variables.number_bacteria):
        number_times_bacterium_exists = random.sample(range(int(variables.min_proportion_bacteria*variables.number_individuals), int(variables.max_proportion_bacteria*variables.number_individuals)), 1)
        individuals_with_bacteria = random.sample(range(0, variables.number_individuals), number_times_bacterium_exists[0])
        for each_individual in individuals_with_bacteria:
            bacteria_data[each_individual][each_bacterium] = 1

    return (bacteria_data)

        
