#!/bin/bash
#SBATCH --job-name=tstVenus
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G
#SBATCH --time=24:00:00
#SBATCH --partition=zhanglab.p
#SBATCH --output=/srv/disk00/cheyul1/Venus/06-27-21/run6/run6.log

python3 /srv/disk00/cheyul1/Venus/Venus.py \
--read1 /srv/disk00/cheyul1/Venus/data/paired-end1.fastq \
--read2 /srv/disk00/cheyul1/Venus/data/paired-end2.fastq \
--outDir /srv/disk00/cheyul1/Venus/06-27-21/run6/

# python3 /srv/disk00/cheyul1/Venus/Venus.py \
# --read1 /srv/disk00/cheyul1/Venus/data/single-cell1.fastq \
# --read2 /srv/disk00/cheyul1/Venus/data/single-cell2.fastq \
# --outDir /srv/disk00/cheyul1/Venus/06-27-21/run6/ \
# --singleCBstart 1 \
# --singleCBlen 16 \
# --singleUMIstart 17 \
# --singleUMIlen 10 \
# --singleWhitelist /srv/disk00/cheyul1/excessSTAR-2.7.8a/indices/737K-august-2016.txt