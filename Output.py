import csv

### Deletes the header lines ###
no_header_file = open("no_header.txt", "x")
with open('Aligned.out.sam', 'r') as header:
    for line in header.readlines():
        if '@' not in line:
            no_header_file.write(line)
no_header_file.close()


### Cut only the Species column ###
repeat_species_file = open("repeat_species.txt", "x")
with open("no_header.txt") as no_header:
    repeat_species = csv.reader(no_header, delimiter="\t")
    for row in repeat_species:
        repeat_species_file.write(row[2])
        repeat_species_file.write("\n")
repeat_species_file.close()


### Obtains the Unique species ###
repeat_species_file = open("repeat_species.txt", "r")
unique_species_file = open("unique_species.txt", "x")
unique_species_lines = set(repeat_species_file.readlines())
unique_species_file.writelines(set(unique_species_lines))
repeat_species_file.close()
unique_species_file.close()


### Writes the mapped virus species output file ###
with open("repeat_species.txt") as repeat_species_file:
    for i, l in enumerate(repeat_species_file):
        pass
    total_reads = i + 1
print(total_reads)
repeat_species_file.close()


### Matches the virus gi no. to species name ###
venus_output_file = open("venus_output.txt", "x")
with open("unique_species.txt") as unique_species_file:
    for species in unique_species_file.readlines():
        species = species.replace("\n", "")
        print(species)
        virus_species = csv.reader(open("virus.species.txt"), delimiter="\t")
        for row in virus_species:
            if species == row[0]:
                venus_output_file.write(row[1] + "\t")
        count_reads = 0
        for line in open("repeat_species.txt").readlines():
            if species == line.replace("\n", ""):
                count_reads += 1
        venus_output_file.write(str(count_reads) + "\t")
        venus_output_file.write(str(count_reads / (total_reads * 1.0) * 100) + "%")
        venus_output_file.write("\n")

venus_output_file.close()

reader = csv.reader(open("venus_output.txt"), delimiter="\t")

sorted_venus_output = open("sorted_venus_output.txt", "x")
for line in sorted(reader, key=lambda row: row[2], reverse=True):
    for item in line:
        sorted_venus_output.write(item + "\t")
    sorted_venus_output.write("\n")