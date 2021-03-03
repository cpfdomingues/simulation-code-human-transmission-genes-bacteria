import csv
import variables

def write_data (data):

    """
    Writes a file with the number of virulence and resistance genes that each individual has, the presence or abscence of bacteria and the cycle
    """


    name = "data_cycle".strip()+str(variables.number_cycles).strip()+"_p"+str(variables.prob_transmission_resistance_genes).strip()+"_t".strip()+str(variables.loss_rate_resistance_genes).strip()+"_pbp".strip()+str(variables.prob_transmission_bacteria).strip()+".csv".strip()
    with open(name, 'w', newline='') as csvfile:
        file_to_write = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file_to_write.writerow(["Virulence_Genes".strip()+','.strip()+ "Resistance_Genes".strip()+','.strip()+"With_Bacteria".strip()+','.strip()+ "Cycle".strip()])
        for each_line in range(0, len(data)):
            file_to_write.writerow([str(data[each_line][0]).strip()+','.strip()+ str(data[each_line][1]).strip()+','.strip()+ str(data[each_line][2]).strip()+','.strip()+ str(data[each_line][3]).strip()])
                




           

                      
