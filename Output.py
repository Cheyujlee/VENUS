# ## First deletes the header lines ###
# no_header = open("no_head.uniq.chr.txt", "x")

# with open('Aligned.out.sam', 'r') as header:
#     for line in header.readlines():
#         if '@' not in line:
#             no_header.write(line)

import csv

input_file = "Aligned.out.sam"
output_file = open("no.header_unique_only.chr.txt", "x")
with open(input_file) as to_read:
    with open(output_file) as to_write:
        