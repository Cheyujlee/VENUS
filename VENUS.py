import argparse
import os

### Creates the Argument Parser object ###
parser = argparse.ArgumentParser(description="subtractive analysis of viral bulk single-end RNA-seq")


### Specifies the argument for Bulk Single-end RNA-seq ###
parser.add_argument("--read1", type=str, required=True,
                    help="read1 of bulk single-end RNA-seq")
parser.add_argument("--indexDir", type=str, required=True,
                    help="genome index directory")
parser.add_argument("--outDir", type=str, required=False, 
                    help="directory to store output")
args = parser.parse_args()


### Concatenate and run command in bash ###
cmd="STAR " + \
    "--runThreadN 16 " + \
    "--outFileNamePrefix " + args.outDir + " " \
    "--genomeDir " + args.indexDir + " " \
    "--readFilesIn " + args.read1 + " "
print("Running " + cmd)
os.system(cmd)

### local test ###
# print("{} is read1 and {} is read2; {} is the genomeDir".format(args.read1, args.read2, args.genomeDir))