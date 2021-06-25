import argparse
import os
import sys

# This is the current path to the default human genome index directory
human_indexDir = "/srv/disk00/cheyul1/excessSTAR-2.7.8a/indices/human.genomeDir/"
# This is the current path to the default mega virus index directory
virus_indexDir = "/srv/disk00/cheyul1/excessSTAR-2.7.8a/indices/HIV.genomeDir/"


### Creates the Argument Parser object ###
parser = argparse.ArgumentParser(description="subtractive analysis of viral bulk RNA-seq")


### Specifies the argument for bulk RNA-seq ###
parser.add_argument("--read1", type=str, required=True,
                    help="read1 of bulk RNA-seq (barcode)")
parser.add_argument("--read2", type=str, required=False,
                    help="read2 of bulk RNA-seq (cDNA)")
parser.add_argument("--indexDir", type=str, required=False, default=human_indexDir, 
                    help="user-specified genome index directory")
parser.add_argument("--outDir", type=str, required=False, default=os.getcwd(), 
                    help="directory to store output")
args = parser.parse_args()


### Organizes the output directories for human then virus mappings ###
try:
    os.chdir(args.outDir)
    print("Current working directory: {0}".format(os.getcwd()))
except:
    print("An error has occured while changing into '{0}' directory".format(args.outDir))
    sys.exit()

try:
    human_outDir = os.getcwd() + "/human/" 
    os.mkdir(human_outDir)
    virus_outDir = os.getcwd() + "/virus/" 
    os.mkdir(virus_outDir)
except:
    print("An error has occured while making directories in '{0}' directory".format(args.outDir))
    sys.exit()


### Concatenate and run the human mapping in bash ###
if args.read2:
    cmd="STAR " + \
        "--runThreadN 16 " + \
        "--outFileNamePrefix " + human_outDir + " " \
        "--genomeDir " + args.indexDir + " " \
        "--readFilesIn " + args.read2 + " " + args.read1 + " " \
        "--outReadsUnmapped Fastx " + \
        "--outSAMtype None"
else:
    cmd="STAR " + \
        "--runThreadN 16 " + \
        "--outFileNamePrefix " + human_outDir + " " \
        "--genomeDir " + args.indexDir + " " \
        "--readFilesIn " + args.read1 + " " \
        "--outReadsUnmapped Fastx " + \
        "--outSAMtype None"
# os.system(cmd)  # Command run
print("Running " + cmd)


### Appropriately renames the indexDir and read1, read2 for the virus mapping ###
args.indexDir=virus_indexDir
args.read1=human_outDir + "Unmapped.out.mate1.fastq"
# os.rename(human_outDir + "Unmapped.out.mate1", args.read1)
if args.read2:
    args.read2=human_outDir + "Unmapped.out.mate2.fastq"
    # os.rename(human_outDir + "Unmapped.out.mate2", args.read2)


### Concatenate and run the virus mapping in bash ###
if args.read2:
    cmd="STAR " + \
        "--runThreadN 16 " + \
        "--outFileNamePrefix " + virus_outDir + " " \
        "--genomeDir " + args.indexDir + " " \
        "--readFilesIn " + args.read1 + " " + args.read2 + " " \
        "--outFilterMultimapNmax 1"
else:
    cmd="STAR " + \
        "--runThreadN 16 " + \
        "--outFileNamePrefix " + virus_outDir + " " \
        "--genomeDir " + args.indexDir + " " \
        "--readFilesIn " + args.read1 + " " \
        "--outFilterMultimapNmax 1"
# os.system(cmd)  # Command run
print("Running " + cmd)


### local tests ###
# print("{} is read1 and {} is read2; {} is the genomeDir".format(args.read1, args.read2, args.genomeDir))
