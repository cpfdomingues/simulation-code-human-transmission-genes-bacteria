import variables
import random

def connections():
    
    """
    Returns a list with the connections of the simulation based on the number of individuals, the number of neighbors and the type of network chosen 
    """

    individuals = range(1,variables.number_individuals+1)
    individuals = [each_individual for each_individual in individuals for i in range(variables.margin_neighbors)]
    individuals_to_connect = []

    #Construct a regular network
    for each_individual in range(0, len(individuals), 2):
        for i in [1,2]:
            individual_to_add = (individuals[each_individual]+i)%variables.number_individuals       
            if individual_to_add == 0:
                individual_to_add = variables.number_individuals
            individuals_to_connect.append(individual_to_add)
    possible_connections = [individuals, individuals_to_connect]
    
    #Check if each individual individual's first connection changes
    #In case the connection changes, defines a new connection (one that doesn't exist yet)
    for each_connection in range(0, len(possible_connections[0]), 2):
        if random.random() <= variables.network_type:
            out_while = True
            i = 1
            while out_while:
                i = i +1
                new_individual = random.sample(range(1,variables.number_individuals+1), 1)[0]
                individual_1 = possible_connections[0][each_connection]
                line = 0
                while line <= len(possible_connections):
                    line_to_verify = [possible_connections[0][line], possible_connections[1][line]]
                    if ((individual_1 in line_to_verify) and (new_individual in line_to_verify)):
                        out_while = True
                        line = len(possible_connections)+1
                    else:
                        out_while = False
                        line = line +1
            possible_connections[1][each_connection] = new_individual

    #Check if each individual individual's second connection changes
    #In case the connection changes, defines a new connection (one that doesn't exist yet)
    for each_connection in range(1, len(possible_connections[0]), 2):
        if random.random() <= variables.network_type:
            out_while = True
            while out_while:
                new_individual = random.sample(range(1,variables.number_individuals+1), 1)[0]
                individual_1 = possible_connections[0][each_connection]
                line = 0
                while line <= len(possible_connections):
                    line_to_verify = [possible_connections[0][line], possible_connections[1][line]]
                    if ((individual_1 in line_to_verify) and (new_individual in line_to_verify)):
                        out_while = True
                        line = len(possible_connections)+1
                    else:
                        out_while = False
                        line = line +1
            possible_connections[1][each_connection] = new_individual

    return (possible_connections)



