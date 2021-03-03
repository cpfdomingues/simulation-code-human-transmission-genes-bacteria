import variables
import random
import copy
import time
import distribution
import statistics

def contacts_and_antibiotic(virulence_genes_data, resistance_genes_data, bacteria_data, possible_connections):

    """
    Performs all contacts and consequent transmission of virulence and resistance genes and bacteria between individuals. In addition, simulates the administration of antibiotics;

    Requires:
    - virulence_genes_data, a list of lists, each list having the virulence genes of an individual
    - resistance_genes_data, a list of lists, each list having the resistance genes of an individual
    - bacteria_data, a list of lists, each list having the bacteria of an individual
    - possible_connections, a list with the connections of the simulation

    Ensures: a list with the number of virulence genes, resistance genes and information on the presence or absence of bacteria for each individual, for each cycle
    """

    data_last = []
    antibiotic_by_cycle = []
    for each_cycle in range(1, variables.number_cycles+1):
        antibiotic_in_cycle = 0
        virulence_genes_current_data = copy.deepcopy(virulence_genes_data)
        resistance_genes_current_data = copy.deepcopy(resistance_genes_data)
        bacteria_current_data = copy.deepcopy(bacteria_data)

        #Iterate over all connections
        for each_connection in range(0, len(possible_connections[0])):
            individual_1 = (possible_connections[0][each_connection])-1
            individual_2 = (possible_connections[1][each_connection])-1

            #Check the genes and bacteria of individual 1 and 2
            virulence_genes_ind_1 = [virulence_genes_ind_1 for virulence_genes_ind_1 in range(len(virulence_genes_data[individual_1])) if virulence_genes_data[individual_1][virulence_genes_ind_1] == 1]
            resistance_genes_ind_1 = [resistance_genes_ind_1 for resistance_genes_ind_1 in range(len(resistance_genes_data[individual_1])) if resistance_genes_data[individual_1][resistance_genes_ind_1] == 1]
            bacteria_ind_1 = [bacteria_ind_1 for bacteria_ind_1 in range(len(bacteria_data[individual_1])) if bacteria_data[individual_1][bacteria_ind_1] == 1]
            virulence_genes_ind_2 = [virulence_genes_ind_2 for virulence_genes_ind_2 in range(len(virulence_genes_data[individual_2])) if virulence_genes_data[individual_2][virulence_genes_ind_2] == 1]
            resistance_genes_ind_2 = [resistance_genes_ind_2 for resistance_genes_ind_2 in range(len(resistance_genes_data[individual_2])) if resistance_genes_data[individual_2][resistance_genes_ind_2] == 1]
            bacteria_ind_2 = [bacteria_ind_2 for bacteria_ind_2 in range(len(bacteria_data[individual_2])) if bacteria_data[individual_2][bacteria_ind_2] == 1]

            #Transmission from individual 1 to individual 2
            #Bacteria transmission
            if len(bacteria_ind_1) != 0:
                bacteria_transmit_list = [random.random() for x in range(0, len(bacteria_ind_1))]
                number_bacteria_transmit = sum(1 for i in bacteria_transmit_list if i<variables.prob_transmission_bacteria)
                positions_bacteria_transmit = random.sample(bacteria_ind_1, number_bacteria_transmit)
                for each_bacterium in positions_bacteria_transmit:
                    bacteria_current_data[individual_2][each_bacterium] = 1
                    
            #Transmit virulence genes
            if len(virulence_genes_ind_1) != 0:
                virulence_genes_transmit_list = [random.random() for x in range(0, len(virulence_genes_ind_1))]
                number_virulence_genes_transmit = sum(1 for i in virulence_genes_transmit_list if i<variables.prob_transmission_virulence_genes)
                positions_virulence_genes_transmit = random.sample(virulence_genes_ind_1, number_virulence_genes_transmit)        
                for each_virulence_gene in positions_virulence_genes_transmit:
                    virulence_genes_current_data[individual_2][each_virulence_gene] = 1
  
            #Transmit resistance genes
            if len(resistance_genes_ind_1) != 0:
                resistance_genes_transmit_list = [random.random() for x in range(0, len(resistance_genes_ind_1))]
                number_resistance_genes_transmit = sum(1 for i in resistance_genes_transmit_list if i<variables.prob_transmission_resistance_genes)
                positions_resistance_genes_transmit = random.sample(resistance_genes_ind_1, number_resistance_genes_transmit)
                for each_resistance_gene in positions_resistance_genes_transmit:
                    resistance_genes_current_data[individual_2][each_resistance_gene] = 1


            #Transmission from individual 2 to individual 1
            #Bacteria transmission
            if len(bacteria_ind_2) != 0:
                bacteria_transmit_list = [random.random() for x in range(0, len(bacteria_ind_2))]
                number_bacteria_transmit = sum(1 for i in bacteria_transmit_list if i<variables.prob_transmission_bacteria)
                positions_bacteria_transmit = random.sample(bacteria_ind_2, number_bacteria_transmit)
                for each_bacterium in positions_bacteria_transmit:
                    bacteria_current_data[individual_1][each_bacterium] = 1

            #Transmit virulence genes
            if len(virulence_genes_ind_2) != 0:
                virulence_genes_transmit_list = [random.random() for x in range(0, len(virulence_genes_ind_2))]
                number_virulence_genes_transmit = sum(1 for i in virulence_genes_transmit_list if i<variables.prob_transmission_virulence_genes)
                positions_virulence_genes_transmit = random.sample(virulence_genes_ind_2, number_virulence_genes_transmit)
                for each_virulence_gene in positions_virulence_genes_transmit:
                    virulence_genes_current_data[individual_1][each_virulence_gene] = 1
     
            #Transmit resistance genes
            if len(resistance_genes_ind_2) != 0:
                resistance_genes_transmit_list = [random.random() for x in range(0, len(resistance_genes_ind_2))]
                number_resistance_genes_transmit = sum(1 for i in resistance_genes_transmit_list if i<variables.prob_transmission_resistance_genes)
                positions_resistance_genes_transmit = random.sample(resistance_genes_ind_2, number_resistance_genes_transmit)
                for each_resistance_gene in positions_resistance_genes_transmit:
                    resistance_genes_current_data[individual_1][each_resistance_gene] = 1

        virulence_genes_data = copy.deepcopy(virulence_genes_current_data)
        resistance_genes_data = copy.deepcopy(resistance_genes_current_data)
        
        #Check the individuals that have to take antibiotic
        for each_individual in range(0,variables.number_individuals):

            #See if individuals have bacteria, and if so, which ones
            antibiotic_take = False
            bacteria_individual = []
            for each_bacterium in range(0,len(bacteria_data[each_individual])):
                if bacteria_data[each_individual][each_bacterium] == 1:
                    antibiotic_take = True
                    bacteria_individual.append(each_bacterium)                                
            if antibiotic_take:
                antibiotic_in_cycle += 1
                bacteria_to_eliminate = random.sample(bacteria_individual, 1)
                bacteria_to_eliminate = bacteria_to_eliminate[0]
                bacteria_current_data[each_individual][bacteria_to_eliminate] = 0
                antibiotic = bacteria_to_eliminate+1
                variables.number_target_genes = variables.number_resistance_genes//variables.number_antibiotics
                target_genes_lower_limit = (antibiotic * variables.number_target_genes - (variables.number_target_genes + 1))+1
                target_genes_upper_limit = (antibiotic * variables.number_target_genes)-1
                target_genes = list(range(target_genes_lower_limit, target_genes_upper_limit +1))
                for each_gene_active in target_genes:
                    resistance_genes_data[each_individual][each_gene_active] = 1
            
                #Eliminate resistance genes unrelated to the administered antibiotic
                all_genes = list(range(0, variables.number_resistance_genes))
                resistance_genes_not_target = [resistance_genes_not_target for resistance_genes_not_target in all_genes if resistance_genes_not_target not in target_genes]
                resistance_genes_eliminate = [resistance_genes_eliminate for resistance_genes_eliminate in resistance_genes_not_target if resistance_genes_data[each_individual][resistance_genes_eliminate] == 1]
                if len(resistance_genes_eliminate) >= 1:
                    resistance_genes_eliminate_list = [random.random() for x in range(0, len(resistance_genes_eliminate))]
                    number_resistance_genes_eliminate = sum(1 for i in resistance_genes_eliminate_list if i<variables.prob_antibiotic_eliminate_resistance_genes)
                    positions_resistance_genes_eliminate = random.sample(resistance_genes_eliminate, number_resistance_genes_eliminate)
                    for each_resistance_genes_eliminate in positions_resistance_genes_eliminate:
                        resistance_genes_data[each_individual][each_resistance_genes_eliminate] = 0

                #Loss rate for resistance genes not associated with the antibiotic taken
                all_genes = list(range(0, variables.number_resistance_genes))
                resistance_genes_not_target = [resistance_genes_not_target for resistance_genes_not_target in all_genes if resistance_genes_not_target not in target_genes]
                resistance_genes_eliminate_moment = [resistance_genes_eliminate_moment for resistance_genes_eliminate_moment in resistance_genes_not_target if resistance_genes_data[each_individual][resistance_genes_eliminate_moment] == 1]
                if len(resistance_genes_eliminate_moment) >= 1:
                    resistance_genes_eliminate_list = [random.random() for x in range(0, len(resistance_genes_eliminate_moment))]
                    number_resistance_genes_eliminate = sum(1 for i in resistance_genes_eliminate_list if i<variables.loss_rate_resistance_genes)
                    positions_resistance_genes_eliminate = random.sample(resistance_genes_eliminate_moment, number_resistance_genes_eliminate)
                    for each_resistance_genes_eliminate in positions_resistance_genes_eliminate:
                        resistance_genes_data[each_individual][each_resistance_genes_eliminate] = 0

                #Eliminate virulence genes
                virulence_genes_individual = [virulence_genes_individual for virulence_genes_individual in range(len(virulence_genes_data[each_individual])) if virulence_genes_data[each_individual][virulence_genes_individual] == 1]
                virulence_genes_eliminate_list = [random.random() for x in range(0, len(virulence_genes_individual))]
                number_virulence_genes_eliminate = sum(1 for i in virulence_genes_eliminate_list if i<variables.prob_antibiotic_eliminate_virulence_genes)
                positions_virulence_genes_eliminate = random.sample(virulence_genes_individual,number_virulence_genes_eliminate)
                for each_virulence_gene in positions_virulence_genes_eliminate:
                    virulence_genes_data[each_individual][each_virulence_gene] = 0

            #Loss rate for resistance genes          
            else: 
                resistance_genes_moment = [resistance_genes_moment for resistance_genes_moment in range(len(resistance_genes_data[each_individual])) if resistance_genes_data[each_individual][resistance_genes_moment] == 1]                
                resistance_genes_eliminate_list = [random.random() for x in range(0, len(resistance_genes_moment))]
                number_resistance_genes_eliminate = sum(1 for i in resistance_genes_eliminate_list if i<variables.loss_rate_resistance_genes)
                positions_resistance_genes_eliminate = random.sample(resistance_genes_moment, number_resistance_genes_eliminate)
                for each_resistance_genes_eliminate in positions_resistance_genes_eliminate:
                    resistance_genes_data[each_individual][each_resistance_genes_eliminate] = 0
            
        bacteria_data = copy.deepcopy(bacteria_current_data)

        #Insert each of the bacteria in an individual per cycle
        for each_bacterium in range(0,variables.number_bacteria):
            number_times_bacteria_present = 1
            individuals_with_bacteria = random.sample(range(0, variables.number_individuals), number_times_bacteria_present)
            for each_individual in individuals_with_bacteria:
                bacteria_data[each_individual][each_bacterium] = 1

        #Count the genes and bacteria of each individual in each cycle
        for cada_ind in range(0, variables.number_individuals):
            virulence_genes_individual = sum(1 for i in virulence_genes_data[cada_ind] if i==1)
            resistance_genes_individual = sum(1 for i in resistance_genes_data[cada_ind] if i==1)
            bacteria_individual = sum(1 for i in bacteria_data[cada_ind] if i==1)
            list_to_add = [virulence_genes_individual, resistance_genes_individual, bacteria_individual, each_cycle]
            data_last.append(list_to_add)

        antibiotic_by_cycle.append(antibiotic_in_cycle)

    return (data_last)


                

            

            
