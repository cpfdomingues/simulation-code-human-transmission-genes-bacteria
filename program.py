import connections
import time
import distribution
import contacts
import variables
import write_files

possible_connections = connections.connections()
virulence_genes_data = distribution.virulence_genes()
resistance_genes_data = distribution.resistance_genes()
bacteria_data = distribution.bacteria()
data = contacts.contacts_and_antibiotic(virulence_genes_data, resistance_genes_data, bacteria_data, possible_connections)
write_files.write_data(data)
