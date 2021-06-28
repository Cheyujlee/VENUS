import argparse
import os
import sys
import csv

# This is the current path to the virus species metatable
virus_species_metatable = "/srv/disk00/cheyul1/excessSTAR-2.7.8a/virus.species.txt"
# virus_species_metatable = "virus.species.txt"                                   # For local testing

def get_count(line):
    """
    Obtains the read counts from the initially unsorted venus.out.tsv.
    """
    line_fields = line.strip().split("\t")
    return int(line_fields[1])

# 1. Creates the species_reads txt file.
#    This will be used to count the total reads
#    and to create the unique species txt file. 
os.chdir(args.outDir)
with open("species_reads.txt", "x") as species_reads:
    # with open("Aligned.out.sam") as aligned:                                    # For local testing
    with open(os.getcwd() + "/virus/" + "Aligned.out.sam", "r") as aligned:
        reads_total = 0
        for line in aligned.readlines():
            if "@" not in line:
                species_id = line.strip().split("\t")[2]
                species_reads.write(species_id)
                species_reads.write("\n")
                reads_total += 1


# 2. Creates the species txt file.
#    This will be used to loop over the unique species
#    thus counting the reads and writing the Venus output
with open("species_reads.txt") as species_reads: 
    with open("species.txt", "x") as species:
        species.writelines(set(species_reads.readlines()))


# 3. Creates the venus output tsv file.
#    Per row/specie, there will be:
#    specie name | reads count | reads total | reads % of total
venus = open("venus.out.tsv", "x")
venus.close()
with open("venus.out.tsv", "a") as venus:
    with open("species.txt") as species:
        for specie in species.readlines():
            specie = specie.replace("\n", "")
            with open(virus_species_metatable) as metatable:
                metareader = csv.reader(metatable, delimiter="\t")
                for row in metareader:
                    if specie == row[0]:
                        venus.write(row[1] + "\t")
            with open("species_reads.txt") as species_reads:
                reads_count = 0
                for line in species_reads.readlines():
                    if specie == line.replace("\n", ""):
                        reads_count += 1
                venus.write(str(reads_count) + "\t")
            venus.write(str(reads_total) + "\t")
            venus.write(str(reads_count / (reads_total * 1.0)  * 100) + "%")
            venus.write("\n")



# 4. Sorts the venus output tsv file.
#    It first reads the lines to sort,
#    then it overwrites the venus output.
with open("venus.out.tsv") as venus:
    venus_lines = venus.readlines()
    venus_lines.sort(key=get_count, reverse=True)

with open("venus.out.tsv", "w") as venus:
    for line in venus_lines:
        venus.write(line)

os.remove(os.getcwd() + "/species_reads.txt")
os.remove(os.getcwd() + "/species.txt")