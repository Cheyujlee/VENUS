import argparse
import os
import sys

# This is the path to the default human genome index directory

# This is the path to the default mega virus index directory


### Creates the Argument Parser object ###
parser = argparse.ArgumentParser(description="subtractive analysis of viral bulk single-end RNA-seq")


### Specifies the argument for Bulk Single-end RNA-seq ###
parser.add_argument("--read1", type=str, required=True,
                    help="read1 of bulk RNA-seq")
parser.add_argument("--read2", type=str, required=False,
                    help="read2 of bulk RNA-seq")
parser.add_argument("--indexDir", type=str, required=False,
                    help="user-specified genome index directory")
parser.add_argument("--outDir", type=str, required=False, default=os.getcwd(), 
                    help="directory to store output")
args = parser.parse_args()


### Organizes the output directories
try:
    os.chdir(args.outDir)
    print("Current working directory: {0}".format(os.getcwd()))

    os.mkdir(os.getcwd() + "/human/")
    os.mkdir(os.getcwd() + "/virus/")
except:
    print("An error has occured while changing into '{0}' directory".format(args.outDir))
    sys.exit()


### Concatenate and run command in bash ###
cmd="STAR " + \
    "--runThreadN 16 " + \
    "--outFileNamePrefix " + args.outDir + " " \
    "--genomeDir " + args.indexDir + " " \
    "--readFilesIn " + args.read1 + " "
# os.system(cmd)  # Command run
print("Running " + cmd)


### local tests ###
# print("{} is read1 and {} is read2; {} is the genomeDir".format(args.read1, args.read2, args.genomeDir))
